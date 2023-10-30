import re
import sys
import random
import string
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QSpinBox, QMessageBox
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from gui import PassGuard

def check_password_strength(password):
    # Your password strength checking code here
    password = password.strip()

    if not password:
        return "Weak: Password is empty."
    if len(password) < 8:
        return "Weak: Password is too short."
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Weak: Include at least one digit."
    if not re.search(r'[!@#$%^&*()-_+=]', password):
        return "Weak: Include at least one special character."
    return "Strong: Password meets recommended criteria."

def generate_random_password(uppercase, lowercase, digits, special_chars, length):
    if not (uppercase or lowercase or digits or special_chars):
        return "Weak: Please select at least one character type."

    char_sets = ""
    if uppercase:
        char_sets += string.ascii_uppercase
    if lowercase:
        char_sets += string.ascii_lowercase
    if digits:
        char_sets += string.digits
    if special_chars:
        char_sets += "!@#$%^&*()-_+="

    if not char_sets:
        return "Weak: No character sets selected."

    return ''.join(random.choice(char_sets) for _ in range(length))

def check_strength():
    password = window.password_input.text()
    strength = check_password_strength(password)
    window.result_label.setText(strength)
    set_strength_label_color(window, strength)

    if "Weak" in strength and "empty" not in strength:
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Warning)
        message_box.setWindowTitle("Password Strength Warning")
        message_box.setText("The password is weak. Please choose a stronger password.")
        message_box.exec()

def generate_password():
    uppercase = window.uppercase_checkbox.isChecked()
    lowercase = window.lowercase_checkbox.isChecked()
    digits = window.digits_checkbox.isChecked()
    special_chars = window.special_chars_checkbox.isChecked()
    length = int(window.length_input.text())
    
    random_password = generate_random_password(uppercase, lowercase, digits, special_chars, length)
    window.password_input.setText(random_password)
    window.result_label.setText("")  # Clear the result label
    set_strength_label_color(window, "Strong:")

def set_strength_label_color(window, strength):
    if strength.startswith("Strong"):
        color = QColor(Qt.GlobalColor.green)
    elif strength.startswith("Weak"):
        color = QColor(Qt.GlobalColor.red)
    else:
        color = QColor(Qt.GlobalColor.black)
    
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.WindowText, color)
    window.result_label.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use the Fusion style
    window = PassGuard()
    window.set_check_strength_callback(check_strength)
    window.generate_button.clicked.connect(generate_password)
    window.show()
    sys.exit(app.exec())
