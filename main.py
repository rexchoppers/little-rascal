from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                               QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, 
                               QTextEdit, QLabel)
from PyQt5.QtCore import Qt

class LittleRascalApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Little Rascal")
        self.setGeometry(100, 100, 600, 500)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Create the four sections
        self.create_section_one(main_layout)
        self.create_section_two(main_layout)
        self.create_section_three(main_layout)
        self.create_section_four(main_layout)

    def create_section_one(self, parent_layout):
        # Section 1: Clear and Secure buttons
        section_one = QGroupBox()
        layout = QVBoxLayout()

        clear_button = QPushButton("Clear")
        clear_button.setStyleSheet("background-color: lightblue;")
        secure_button = QPushButton("Secure")
        secure_button.setStyleSheet("background-color: red;")

        layout.addWidget(clear_button)
        layout.addWidget(secure_button)

        section_one.setLayout(layout)
        parent_layout.addWidget(section_one)

    def create_section_two(self, parent_layout):
        # Section 2: Text display, Next and Delete buttons
        section_two = QGroupBox()
        layout = QVBoxLayout()

        # Text display
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)

        # Buttons layout
        buttons_layout = QVBoxLayout()
        next_button = QPushButton("Next")
        delete_button = QPushButton("Delete")

        buttons_layout.addWidget(next_button)
        buttons_layout.addWidget(delete_button)

        layout.addWidget(self.text_display)
        layout.addLayout(buttons_layout)

        section_two.setLayout(layout)
        parent_layout.addWidget(section_two)

    def create_section_three(self, parent_layout):
        # Section 3: Numeric buttons (0-9) and SELECT
        section_three = QGroupBox()
        layout = QGridLayout()

        # Row 1: 0, 1, 2, 3
        layout.addWidget(QPushButton("0"), 0, 0)
        layout.addWidget(QPushButton("1"), 0, 1)
        layout.addWidget(QPushButton("2"), 0, 2)
        layout.addWidget(QPushButton("3"), 0, 3)

        # Row 2: 4, 5, 6
        layout.addWidget(QPushButton("4"), 1, 0)
        layout.addWidget(QPushButton("5"), 1, 1)
        layout.addWidget(QPushButton("6"), 1, 2)

        # Row 3: SELECT, 7, 8, 9
        layout.addWidget(QPushButton("SELECT"), 2, 0)
        layout.addWidget(QPushButton("7"), 2, 1)
        layout.addWidget(QPushButton("8"), 2, 2)
        layout.addWidget(QPushButton("9"), 2, 3)

        section_three.setLayout(layout)
        parent_layout.addWidget(section_three)

    def create_section_four(self, parent_layout):
        # Section 4: Letter buttons and special function buttons
        section_four = QGroupBox()
        layout = QGridLayout()

        # Row 1: A, B, +, Enter
        layout.addWidget(QPushButton("A"), 0, 0)
        layout.addWidget(QPushButton("B"), 0, 1)
        layout.addWidget(QPushButton("Enter"), 0, 2)

        # Row 2: C, D, FILL
        layout.addWidget(QPushButton("C"), 1, 0)
        layout.addWidget(QPushButton("D"), 1, 1)
        layout.addWidget(QPushButton("FILL"), 1, 2, 1, 2)  # Span 2 columns

        # Row 3: E, F, ERASE
        layout.addWidget(QPushButton("E"), 2, 0)
        layout.addWidget(QPushButton("F"), 2, 1)
        layout.addWidget(QPushButton("ERASE"), 2, 2, 1, 2)  # Span 2 columns

        section_four.setLayout(layout)
        parent_layout.addWidget(section_four)


if __name__ == "__main__":
    app = QApplication([])
    window = LittleRascalApp()
    window.show()
    app.exec_()
