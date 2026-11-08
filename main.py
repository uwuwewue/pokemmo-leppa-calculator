import sys
import ctypes
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, 
    QLabel, QLineEdit, QVBoxLayout, QFrame
)

class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leppa Profit Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumWidth(380)

        self.title_label = QLabel("Leppa Berry Calculator")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.characters_amount_label = QLabel("How many characters do you use?")
        self.characters_amount_input = QLineEdit()
        self.characters_amount_input.setPlaceholderText("e.g. 4")
        
        self.very_spicy_seed_label = QLabel("How much does ONE Very Spicy Seed cost?")
        self.very_spicy_seed_input = QLineEdit()
        self.very_spicy_seed_input.setPlaceholderText("e.g. 1100")
        
        self.plain_bitter_seed_label = QLabel("How much does ONE Plain Bitter Seed cost?")
        self.plain_bitter_seed_input = QLineEdit()
        self.plain_bitter_seed_input.setPlaceholderText("e.g. 550")
        
        self.plain_sweet_seed_label = QLabel("How much does ONE Plain Sweet Seed cost?")
        self.plain_sweet_seed_input = QLineEdit()
        self.plain_sweet_seed_input.setPlaceholderText("e.g. 550")

        self.how_much_per_stack_label = QLabel("How much does ONE STACK of Leppas cost?")
        self.how_much_per_stack_input = QLineEdit()
        self.how_much_per_stack_input.setPlaceholderText("e.g. 82000")

        self.button = QPushButton("Calculate Profit")
        self.button.setFixedHeight(44)
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.clicked.connect(self.calculate_profit)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setObjectName("separator")

        self.result_label = QLabel("Results will appear here...")
        self.result_label.setObjectName("results")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.UI()
        self.apply_styles()

    def UI(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(24, 24, 24, 24)
        vbox.setSpacing(8)

        vbox.addWidget(self.title_label)
        vbox.addSpacing(10)
        
        vbox.addWidget(self.characters_amount_label)
        vbox.addWidget(self.characters_amount_input)

        vbox.addWidget(self.very_spicy_seed_label)
        vbox.addWidget(self.very_spicy_seed_input)

        vbox.addWidget(self.plain_bitter_seed_label)
        vbox.addWidget(self.plain_bitter_seed_input)

        vbox.addWidget(self.plain_sweet_seed_label)
        vbox.addWidget(self.plain_sweet_seed_input)

        vbox.addWidget(self.how_much_per_stack_label)
        vbox.addWidget(self.how_much_per_stack_input)

        vbox.addSpacing(14)
        vbox.addWidget(self.button)
        vbox.addSpacing(10)
        vbox.addWidget(self.separator)
        vbox.addSpacing(10)
        vbox.addWidget(self.result_label)
        
        self.setLayout(vbox)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 13px;
            }
            QLabel#title {
                font-size: 18px;
                font-weight: bold;
                color: #f38ba8;
            }
            QLineEdit {
                background-color: #313244;
                border: 1px solid #45475a;
                border-radius: 6px;
                padding: 8px 10px;
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #f38ba8;
            }
            QPushButton {
                background-color: #f38ba8;
                color: #11111b;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #eba0ac;
            }
            QPushButton:pressed {
                background-color: #f5c2e7;
            }
            QFrame#separator {
                background-color: #45475a;
                max-height: 1px;
                border: none;
            }
            QLabel#results {
                background-color: #181825;
                border: 1px solid #313244;
                border-radius: 8px;
                padding: 14px;
                font-size: 14px;
                font-weight: bold;
                color: #a6e3a1;
            }
        """)

    def calculate_profit(self):
        try:
            chars = int(self.characters_amount_input.text())
            v_spicy = int(self.very_spicy_seed_input.text())
            p_bitter = int(self.plain_bitter_seed_input.text())
            p_sweet = int(self.plain_sweet_seed_input.text())
            cost_per_stack = int(self.how_much_per_stack_input.text())

            plot_cost = v_spicy + p_bitter + p_sweet
            cost_per_char = plot_cost * 156
            cost = chars * cost_per_char
            revenue = 9 * cost_per_stack * chars
            profit = revenue - cost

            self.result_label.setText(
                f"Revenue: {revenue:,} ¥\n"
                f"Cost: {cost:,} ¥\n"
                f"Profit: {profit:,} ¥"
            )
        except ValueError:
            self.result_label.setText("Error: Please fill in all fields with valid numbers!")

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("leppa.calculator")
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()