import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

# ------------------ IMPORT DECODERS ------------------
from decoder.image_decoder import decode_message as image_decode
from decoder.keystroke_decoder import decode_keystroke
from decoder.clock_decoder import decode_clock
from decoder.document_decoder import decode_document
from decoder.code_decoder import decode_code
from decoder.motion_decoder import decode_motion

# ------------------ THEME COLORS ------------------
BG_CARD = "#0b1220"
BG_WIDGET = "#060b14"
ACCENT = "#00ff9c"
ACCENT_SOFT = "#00c97a"
TEXT_MUTED = "#9aa4b2"
TEXT_MAIN = "#e6fff5"
ERROR = "#ff5f5f"


def decoder_ui(parent):

    parent.configure(fg_color="transparent")

    # ==============================
    # CARD
    # ==============================
    card = ctk.CTkFrame(
        parent,
        fg_color=BG_CARD,
        corner_radius=22,
        border_width=1,
        border_color=ACCENT
    )
    card.pack(fill="both", expand=True, padx=24, pady=24)

    # ==============================
    # HEADER
    # ==============================
    ctk.CTkLabel(
        card,
        text="AGENTX STEGANOGRAPHY DECODER",
        font=("Orbitron", 18, "bold"),
        text_color=TEXT_MAIN
    ).pack(pady=(20, 4))

    ctk.CTkLabel(
        card,
        text="Extract covert intelligence from multiple stego channels",
        font=("Consolas", 11),
        text_color=TEXT_MUTED
    ).pack(pady=(0, 16))

    # ==============================
    # MODE SELECTION
    # ==============================
    ctk.CTkLabel(
        card,
        text="STEGO MODE",
        font=("Consolas", 12, "bold"),
        text_color=ACCENT
    ).pack(anchor="w", padx=30, pady=(8, 4))

    stego_mode = ctk.StringVar(value="Image")

    ctk.CTkOptionMenu(
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
        width=240
    ).pack(anchor="w", padx=30, pady=(6, 14))

    # ==============================
    # FILE SELECTION
    # ==============================
    input_path = ctk.StringVar()

    def browse_file():
        input_path.set(filedialog.askopenfilename())

    ctk.CTkButton(
        card,
        text="📂 SELECT INPUT FILE",
        command=browse_file,
        fg_color=BG_WIDGET,
        hover_color="#0c1a2b",
        text_color=ACCENT,
        width=260,
        height=42,
        corner_radius=12
    ).pack(pady=8)

    ctk.CTkLabel(
        card,
        textvariable=input_path,
        font=("Consolas", 9),
        text_color=TEXT_MUTED,
        wraplength=520
    ).pack(padx=30, pady=(0, 14), anchor="w")

    # ==============================
    # OUTPUT
    # ==============================
    ctk.CTkLabel(
        card,
        text="DECODED MESSAGE",
        font=("Consolas", 12, "bold"),
        text_color=ACCENT
    ).pack(anchor="w", padx=30, pady=(10, 6))

    output_box = ctk.CTkTextbox(
        card,
        height=170,
        corner_radius=16,
        fg_color=BG_WIDGET,
        text_color=ACCENT,
        font=("JetBrains Mono", 11),
        wrap="word"
    )
    output_box.pack(padx=30, pady=(6, 16), fill="x")
    output_box.configure(state="disabled")

    # ==============================
    # STATUS
    # ==============================
    status_label = ctk.CTkLabel(
        card,
        text="STATUS :: Awaiting input",
        font=("Consolas", 10),
        text_color=TEXT_MUTED
    )
    status_label.pack(pady=(0, 10))

    # ==============================
    # DECODE ACTION
    # ==============================
    def decode_action():
        path = input_path.get()
        mode = stego_mode.get()

        if not path:
            status_label.configure(text="STATUS :: No input selected", text_color=ERROR)
            messagebox.showerror("AGENTX", "No input file selected")
            return

        try:
            if mode == "Image":
                message = image_decode(path)

            elif mode == "Keystroke":
                message = decode_keystroke(path)

            elif mode == "Clock":
                message = decode_clock(path)

            elif mode == "Document":
                message = decode_document(path)

            elif mode == "Code":
                message = decode_code(path)

            elif mode == "Motion":
                message = decode_motion(path)

            else:
                raise ValueError("Invalid steganography mode")

            output_box.configure(state="normal")
            output_box.delete("0.0", "end")
            output_box.insert("end", message)
            output_box.configure(state="disabled")

            status_label.configure(
                text="STATUS :: Decode successful",
                text_color=ACCENT_SOFT
            )

        except Exception as e:
            status_label.configure(text="STATUS :: Decode failed", text_color=ERROR)
            messagebox.showerror("AGENTX ERROR", str(e))

    # ==============================
    # DECODE BUTTON
    # ==============================
    ctk.CTkButton(
        card,
        text="🔓 DECODE MESSAGE",
        command=decode_action,
        fg_color=ACCENT,
        hover_color="#00e68a",
        text_color="#020b10",
        font=("Consolas", 13, "bold"),
        width=280,
        height=48,
        corner_radius=16
    ).pack(pady=(6, 24))
