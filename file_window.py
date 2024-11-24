from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton

import sys

class delo(QWidget):
    def __init__(self, filename: str, dir: str):
            super().__init__()
            self.setWindowTitle(filename)
            self.filename = filename
            self.dir = dir
            self.initUI()

    def initUI(self):

        text = self.init_text()

        main_layout = QVBoxLayout()
        hlayout = QHBoxLayout()

        self.line_edit = QTextEdit()
        self.line_edit.setFixedSize(400, 400)
        self.line_edit.setText(text)

        self.savebutton = QPushButton("save")
        self.savebutton.clicked.connect(self.save_file)

        self.exitbutton = QPushButton("exit")
        self.exitbutton.clicked.connect(self.exit)

        hlayout.addWidget(self.savebutton)
        hlayout.addWidget(self.exitbutton)
        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(hlayout)

        self.setLayout(main_layout)

        

    def init_text(self) -> str:
        lines = []
        with open(f"{self.dir}/{self.filename}", "r", encoding="utf-8")as file:
            for line in file:
                lines.append(line)
        return "".join(lines)
    
    def save_file(self):
        text = self.line_edit.toPlainText()

        with open(f"{self.dir}/{self.filename}", "w", encoding="utf-8")as file:
            file.write(text)

    def exit(self):
        self.close()
