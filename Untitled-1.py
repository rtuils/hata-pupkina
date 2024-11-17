import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Введіть ім'я та код")
        self.setGeometry(100, 100, 300, 200)

        
        self.name_label = QLabel("Ваше ім'я:")
        self.name_input = QLineEdit()
        
        self.code_label = QLabel("Шістнадцятизначний код:")
        self.code_input = QLineEdit()

        self.submit_button = QPushButton("Підтвердити")
        self.result_label = QLabel("")

        
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.code_label)
        layout.addWidget(self.code_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

        self.submit_button.clicked.connect(self.on_submit)

        self.setLayout(layout)

    def on_submit(self):
        name = self.name_input.text()
        code = self.code_input.text()

       
        if len(name) == 0 or len(code) != 16 or not code.isdigit():
            self.result_label.setText("Помилка: некоректне введення.")
        else:
            self.result_label.setText(f"Привіт, {name}! Ваш код: {code}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())