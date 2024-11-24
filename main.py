import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit
from file_window import delo

class todo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("delo")
        self.windows = []
        self.dir = "dir"
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.create_button = QPushButton("create_file")
        self.create_button.clicked.connect(self.create_file)
        self.delete_button = QPushButton("delete_file")
        self.delete_button.clicked.connect(self.delete_file)

        self.line_edit = QLineEdit()

        self.button_layout.addWidget(self.line_edit)
        self.button_layout.addWidget(self.create_button)
        self.button_layout.addWidget(self.delete_button)

        self.main_layout.setSpacing(50)
        self.main_layout.addLayout(self.grid_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        self.update_grid_layout()

    def update_grid_layout(self):
        files = os.listdir(self.dir)
        files = sorted(files, key=lambda f: os.path.getctime(os.path.join(self.dir, f)))
        for i, file in enumerate(files):
            pushbutton = QPushButton(file)
            pushbutton.clicked.connect(lambda checked, f=file: self.open_file(f, self.dir))
            self.grid_layout.addWidget(pushbutton, i // 4, i % 4)

    def create_file(self):
        filename = self.line_edit.text()
        if filename: 
            with open(f"{self.dir}/{filename}", "w"):
                pass
            self.update_grid_layout() 
            self.open_file(filename, self.dir)

    def delete_file(self):
        filename = self.line_edit.text()
        if filename in os.listdir(self.dir):
            os.remove(f"{self.dir}/{filename}")
            self.update_grid_layout()

    def open_file(self, filename, dir):
        window = delo(filename, dir)
        self.windows.append(window)
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = todo()
    window.show()
    sys.exit(app.exec())
