import sys
from PySide6.QtWidgets import QApplication, QStackedWidget

# Import screens
from gui.intro_screen import IntroScreen
from gui.overlay_video_screen import OverlayVideoScreen  # ✅ NEW


def start_app():
    app = QApplication(sys.argv)

    # 🧱 Stack (screen manager)
    stack = QStackedWidget()

    # 🎬 Screens
    intro = IntroScreen(stack)
    overlay = OverlayVideoScreen()  # no stack needed here

    # ➕ Add screens in order
    stack.addWidget(intro)     # index 0
    stack.addWidget(overlay)   # index 1

    # 🎥 Start with intro
    stack.setCurrentIndex(0)

    # 🪟 Window settings
    stack.resize(1000, 600)
    stack.setWindowTitle("AGENTX")
    stack.show()

    sys.exit(app.exec())