import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading

# ------------------ IMPORT ENCODERS ------------------
from encoder.image_encoder import encode_message as image_encode
from encoder.keystroke_encoder import encode_keystroke
from encoder.clock_encoder import encode_clock
from encoder.document_encoder import encode_document
from encoder.code_encoder import encode_code
from encoder.motion_encoder import encode_motion

from voice.speech_to_text import listen_from_mic

# ------------------ COLORS ------------------
BG_CARD = "#0b1220"
BG_WIDGET = "#060b14"
ACCENT = "#00ff9c"
TEXT_MUTED = "#9aa4b2"
TEXT_MAIN = "#e6fff5"


def encoder_ui(parent):
    parent.configure(fg_color="transparent")

    # ------------------ CARD ------------------
    card = ctk.CTkFrame(
        parent,
        fg_color=BG_CARD,
        corner_radius=20,
        border_width=1,
        border_color=ACCENT
    )
    card.pack(fill="both", expand=True, padx=20, pady=20)

    # ------------------ TITLE ------------------
    ctk.CTkLabel(
        card,
        text="AGENTX STEGANOGRAPHY ENCODER",
        font=("Orbitron", 16, "bold"),
        text_color=TEXT_MAIN
    ).pack(pady=(18, 6))

    ctk.CTkLabel(
        card,
        text="Select steganography type and encode secret intelligence",
        font=("Consolas", 11),
        text_color=TEXT_MUTED
    ).pack(pady=(0, 16))

    # ------------------ MODE SELECTION ------------------
    ctk.CTkLabel(
        card,
        text="STEGO MODE",
        font=("Consolas", 11, "bold"),
        text_color=ACCENT
    ).pack(anchor="w", padx=24)

    stego_mode = ctk.StringVar(value="Image")

    mode_menu = ctk.CTkOptionMenu(
        card,
        values=[
            "Image",
            "Keystroke",
            "Clock",
            "Document",
            "Code",
            "Motion"
        ],
        variable=stego_mode,
        fg_color=BG_WIDGET,
        button_color=ACCENT,
        button_hover_color="#00e68a",
        text_color=ACCENT,
        width=220
    )
    mode_menu.pack(padx=24, pady=(6, 16), anchor="w")

    # ------------------ MESSAGE ------------------
    ctk.CTkLabel(
        card,
        text="SECRET MESSAGE",
        font=("Consolas", 11, "bold"),
        text_color=ACCENT
    ).pack(anchor="w", padx=24)

    text_box = ctk.CTkTextbox(
        card,
        height=140,
        corner_radius=14,
        fg_color=BG_WIDGET,
        text_color=ACCENT,
        font=("JetBrains Mono", 11)
    )
    text_box.pack(padx=24, pady=(8, 14), fill="x")

    # ------------------ ACTION ROW ------------------
    action_row = ctk.CTkFrame(card, fg_color="transparent")
    action_row.pack(pady=6)

    def voice_input():
        mic_btn.configure(state="disabled")

        def listen():
            try:
                text = listen_from_mic()
                if text:
                    text_box.delete("0.0", "end")
                    text_box.insert("end", text)
            finally:
                mic_btn.configure(state="normal")

        threading.Thread(target=listen, daemon=True).start()

    mic_btn = ctk.CTkButton(
        action_row,
        text="🎤 Voice Input",
        command=voice_input,
        fg_color=BG_WIDGET,
        hover_color="#0a1422",
        text_color=ACCENT,
        width=150
    )
    mic_btn.pack(side="left", padx=6)

    file_path = ctk.StringVar()

    def browse_file():
        file_path.set(
            filedialog.askopenfilename()
        )

    file_btn = ctk.CTkButton(
        action_row,
        text="📂 Select File",
        command=browse_file,
        fg_color=BG_WIDGET,
        hover_color="#0a1422",
        text_color=ACCENT,
        width=180
    )
    file_btn.pack(side="left", padx=6)

    ctk.CTkLabel(
        card,
        textvariable=file_path,
        font=("Consolas", 9),
        text_color=TEXT_MUTED,
        wraplength=520
    ).pack(padx=24, pady=(6, 16), anchor="w")

    # ------------------ ENCODE LOGIC ------------------
    def encode_action():
        mode = stego_mode.get()
        msg = text_box.get("0.0", "end").strip()
        path = file_path.get()

        if not msg:
            messagebox.showerror("AGENTX", "Secret message is empty")
            return

        os.makedirs("output", exist_ok=True)

        try:
            if mode == "Image":
                if not path:
                    raise ValueError("Image file required")
                image_encode(path, msg, "output/encoded_image.png")

            elif mode == "Keystroke":
                encode_keystroke(msg, "output/keystroke.dat")

            elif mode == "Clock":
                encode_clock(msg, "output/clock.txt")

            elif mode == "Document":
                if not path:
                    raise ValueError("Document file required")
                encode_document(path, msg, "output/encoded_doc.txt")

            elif mode == "Code":
                encode_code(msg, "output/code_payload.py")

            elif mode == "Motion":
                encode_motion(msg, "output/motion.log")

            messagebox.showinfo("AGENTX", f"{mode} encoding successful!")

        except Exception as e:
            messagebox.showerror("AGENTX ERROR", str(e))

    # ------------------ ENCODE BUTTON ------------------
    encode_btn = ctk.CTkButton(
        card,
        text="ENCODE & SAVE",
        command=encode_action,
        fg_color=ACCENT,
        hover_color="#00e68a",
        text_color="#020b10",
        font=("Consolas", 12, "bold"),
        width=260,
        height=46,
        corner_radius=14
    )
    encode_btn.pack(pady=(12, 22))
