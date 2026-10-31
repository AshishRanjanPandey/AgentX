from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, QTimer
import os


class OverlayVideoScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ninja Scene")

        # ===============================
        # MAIN LAYOUT
        # ===============================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # ===============================
        # VIDEO BACKGROUND
        # ===============================
        self.video = QVideoWidget(self)
        layout.addWidget(self.video)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(self.audio)
        self.player.setVideoOutput(self.video)

        # 📁 Path to transition video
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.video_path = os.path.join(BASE_DIR, "gui", "assets", "transition.mp4")

        print("Loading transition video:", self.video_path)

        self.player.setSource(QUrl.fromLocalFile(self.video_path))

        # ❌ DO NOT PLAY HERE (important fix)

        # ===============================
        # 🌓 WATERMARK HIDER
        # ===============================
        self.mask = QLabel(self)
        self.mask.setGeometry(700, 400, 300, 200)

        self.mask.setStyleSheet("""
            background: qlineargradient(
                x1:1, y1:1, x2:0, y2:0,
                stop:0 rgba(0,0,0,220),
                stop:1 rgba(0,0,0,0)
            );
        """)

        self.mask.raise_()

    # =========================================
    # ▶️ START VIDEO (CALLED AFTER SWITCH)
    # =========================================
    def start_video(self):
        print("Starting transition video...")

        self.player.play()

        # ⏱️ Show login overlay after delay
        QTimer.singleShot(2000, self.show_login_overlay)

    # =========================================
    # 🔐 LOGIN OVERLAY
    # =========================================
    def show_login_overlay(self):

        # 🔥 Glow background
        self.glow = QFrame(self)
        self.glow.setGeometry(300, 130, 400, 260)

        self.glow.setStyleSheet("""
            background-color: rgba(0,255,200,40);
            border-radius: 20px;
        """)

        self.glow.lower()

        # 🧊 Glass panel
        self.panel = QFrame(self)
        self.panel.setGeometry(310, 140, 380, 240)

        self.panel.setStyleSheet("""
            background-color: rgba(10, 15, 25, 200);
            border-radius: 15px;
            border: 2px solid #00ffc8;
        """)

        # Layout inside panel
        layout = QVBoxLayout(self.panel)
        layout.setContentsMargins(30, 20, 30, 20)
        layout.setSpacing(15)

        # 🔐 Title
        self.label = QLabel("AGENT AUTHENTICATION")
        self.label.setStyleSheet("""
            color: #00ffc8;
            font-size: 16px;
            font-weight: bold;
        """)
        layout.addWidget(self.label)

        # 🔑 Password input
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.password.setStyleSheet("""
            background: rgba(0,0,0,180);
            color: white;
            padding: 8px;
            border-radius: 6px;
            border: 1px solid #00ffc8;
        """)
        layout.addWidget(self.password)

        # 🚀 Button
        self.button = QPushButton("ACCESS SYSTEM")

        self.button.setStyleSheet("""
            background-color: #00ffc8;
            color: black;
            padding: 8px;
            border-radius: 6px;
            font-weight: bold;
        """)
        layout.addWidget(self.button)

        # ℹ️ Info text
        self.info = QLabel("Secure Access Required")
        self.info.setStyleSheet("color: #9aa4b2; font-size: 11px;")
        layout.addWidget(self.info)

        # ===============================
        # ⚡ ANIMATED GLOW EFFECT
        # ===============================
        self.glow_level = 40

        def animate_glow():
            self.glow_level += 5
            if self.glow_level > 120:
                self.glow_level = 40

            self.glow.setStyleSheet(f"""
                background-color: rgba(0,255,200,{self.glow_level});
                border-radius: 20px;
            """)

        self.timer = QTimer()
        self.timer.timeout.connect(animate_glow)
        self.timer.start(100)