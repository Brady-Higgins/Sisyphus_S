from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from Encryption.Diary import Diary
import sys

def init():
    diary = Diary()
    first_login = diary.check_password_file_exists()
    return diary, first_login

class SisyphusApp(QWidget):
    def __init__(self, diary, first_login):
        super().__init__()
        self.diary = diary
        self.first_login = first_login
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Sisyphus")
        self.setGeometry(100, 100, 650, 600)

        # Set up layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Sisyphus: for students")
        title_label.setStyleSheet("font-size: 34px;")
        title_label.setFixedHeight(80)
        layout.addWidget(title_label)

        # Body label based on first login
        if self.first_login:
            body_text = "Welcome, please input your permanent password below and click submit when you're finished"
            
        else:
            body_text = "Welcome back, please enter your password"

        body_label = QLabel(body_text)
        body_label.setStyleSheet("font-size: 20px;")
        body_label.setFixedHeight(60)
        layout.addWidget(body_label)

        # Password entry
        self.text_entry = QLineEdit(self)
        self.text_entry.setEchoMode(QLineEdit.Password)
        self.text_entry.setFixedWidth(400)
        layout.addWidget(self.text_entry)

        # Submit button
        submit_button = QPushButton("Submit", self)
        submit_button.setFixedSize(150, 50)
        submit_button.clicked.connect(self.submit_password)
        layout.addWidget(submit_button)

        # Set the layout for the main widget
        self.setLayout(layout)

    def submit_password(self):
        password_attempt = self.text_entry.text()
        # Replace this with actual verification if diary is set up
        if self.first_login:
            self.diary.createPasswordFile()
            self.diary.createStorageFile(password_attempt)
            self.homepage()
        else:
            self.createEncryptionKey(password_attempt)
            if self.validateIdentity(password_attempt):
                self.homepage()
            else:
                QMessageBox(self,"Message","Incorrect Password Attempt")
                exit()

    def homepage(self):
        pass
def main():
    # Initialize the diary and first_login values
    diary, first_login = init()
    app = QApplication(sys.argv)
    sisyphus_app = SisyphusApp(diary, first_login)
    sisyphus_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
