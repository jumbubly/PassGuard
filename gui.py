import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QSpinBox

class PassGuard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PassGuard")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Enter a password:")
        self.password_input = QLineEdit()
        self.check_button = QPushButton("Check Strength")
        self.result_label = QLabel("")

        # Password generation elements
        self.uppercase_checkbox = QCheckBox("Uppercase")
        self.lowercase_checkbox = QCheckBox("Lowercase")
        self.digits_checkbox = QCheckBox("Digits")
        self.special_chars_checkbox = QCheckBox("Special Characters")
        self.length_label = QLabel("Length:")
        self.length_input = QSpinBox()
        
        # Limit the maximum value of the length input to 32
        self.length_input.setMaximum(32)
        
        self.generate_button = QPushButton("Generate Password")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_label)

        # Add password generation elements to the layout
        generation_layout = QHBoxLayout()
        generation_layout.addWidget(self.uppercase_checkbox)
        generation_layout.addWidget(self.lowercase_checkbox)
        generation_layout.addWidget(self.digits_checkbox)
        generation_layout.addWidget(self.special_chars_checkbox)
        generation_layout.addWidget(self.length_label)
        generation_layout.addWidget(self.length_input)
        generation_layout.addWidget(self.generate_button)

        layout.addLayout(generation_layout)

        self.setLayout(layout)

    def set_check_strength_callback(self, callback):
        self.check_button.clicked.connect(callback)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PassGuard()
    window.show()
    sys.exit(app.exec())
