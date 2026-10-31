from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl
import os


class IntroScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.setWindowTitle("Intro Video")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # ===============================
        # 🎥 VIDEO WIDGET
        # ===============================
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        # ===============================
        # 🎵 MEDIA PLAYER
        # ===============================
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(self.audio)
        self.player.setVideoOutput(self.video_widget)

        # ===============================
        # 📁 VIDEO PATH
        # ===============================
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.video_path = os.path.join(BASE_DIR, "gui", "assets", "intro.mp4")

        print("Loading intro video:", self.video_path)

        self.player.setSource(QUrl.fromLocalFile(self.video_path))

        # ===============================
        # 🔥 DETECT VIDEO END
        # ===============================
        self.player.mediaStatusChanged.connect(self.handle_status)

        # ▶️ START VIDEO
        self.player.play()

    # =========================================
    # 🚀 HANDLE VIDEO END
    # =========================================
    def handle_status(self, status):
        from PySide6.QtMultimedia import QMediaPlayer

        if status == QMediaPlayer.EndOfMedia:
            print("Intro finished → switching screen")

            # 🛑 STOP intro video (VERY IMPORTANT)
            self.player.stop()

            # 🎯 Get next screen
            next_screen = self.stack.widget(1)

            # 🔄 Switch screen
            self.stack.setCurrentIndex(1)

            # ▶️ Start next screen video
            next_screen.start_video()