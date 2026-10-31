from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class LoginScreen(QWidget):
    def __init__(self, stack):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Login Screen (Next Step)")
        btn = QPushButton("Continue")

        layout.addWidget(label)
        layout.addWidget(btn)

        self.setLayout(layout)