# inspection_form.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QScrollArea, QGroupBox, QFormLayout, QTextEdit
from PyQt5.QtCore import Qt

class InspectionForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Main layout for the form
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(50)

        # Title heading
        self.title_label = QLabel("New Inspection")
        self.title_label.setStyleSheet("font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignTop)
        main_layout.addWidget(self.title_label)

        # Create a scrollable area
        scroll_area = QScrollArea()
        scroll_area.setAlignment(Qt.AlignTop)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignTop)

        # Add sections with questions
        sections = ["Inspection Details", "Tires", "Battery", "Exterior", "Brakes", "Engine", "Customer Feedback"]

        questions = [
            ["Truck Serial Number: ", "Truck Model: ", "Inspection ID: ", "Inspector Name: ", "Inspector Employee ID: ", "Date/Time: ", "Location: ", "Geo-cordinates: ", "Service Meter Hours: ", "Customer Name: ", "CAT Customer ID: "],
            ["Tire Pressure Left Front: ", "Tire Pressure Right Front: ", "Tire Condition Left Front: ", "Tire Condition Right Front: ", "Tire Pressure Left Rear: ", "Tire Pressure Right Rear: ", "Tire Condition Left Rear: ", "Tire Condition Right Rear: ", "Tire Summary: "],
            ["Battery Make: ", "Battery Replacement Date: ", "Battery Voltage: ", "Battery Water Level: ", "Condition of Battery: ", "Any Leak/Rust: ", "Battery Summary: "],
            ["Rust, Dent, Damage to exterior: ", "Oil leak in suspension: ", "Exterior Summary: "],
            ["Brake Fluid Level: ", "Brake Condition for Front: ", "Brake Condition for Rear: ", "Emergency Brake: ", "Brake Summary: "],
            ["Rust, Dent, Damage in Engine: ", "Engine Oil Condition: ", "Engine Oil Color: ", "Brake Fluid Condition: ", "Brake Fluid Color: ", "Any oil leak: ", "Engine Summary: "],
            ["Customer Feedback: "]
        ]

        for i, section in enumerate(sections):
            section_group = QGroupBox(section)
            section_layout = QFormLayout(section_group)
        
            for question in questions[i]:
                question_label = QLabel(question)
                question_label.setStyleSheet("font-weight: normal;font-size:16px;")
                text_area = QTextEdit()
                text_area.setStyleSheet("font-weight: normal;font-size:16px;")
                text_area.setFixedHeight(40)
                section_layout.addRow(question_label, text_area)

            section_group.setStyleSheet("font-weight: bold; font-size:20px;")
            scroll_layout.addWidget(section_group)

        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #ffcc21;
                color: #252525;
                font-size: 18px;
                padding: 10px 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #ffdd33;
            }
        """)
        main_layout.addWidget(self.submit_button)

    def submit_inspection(self):
        print("Inspection submitted.")
