from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class RenameDialog(QDialog):
    def __init__(self, old_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rename File")
        self.setStyleSheet("""
        QDialog {
            background-color: #444;
            color: #ffcc21;
            border-radius: 10px;
        }
        QLabel, QLineEdit, QPushButton {
            background-color: #333;
            color: #ffcc21;
            border: 1px solid #ffcc21;
            border-radius: 5px;
            padding: 5px;a
        }
        QPushButton {
            background-color: #555;
        }
        QPushButton:hover {
            background-color: #666;
        }
        """)

        self.old_name = old_name
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel(f"Rename '{self.old_name}':")
        self.line_edit = QLineEdit(self.old_name)
        self.rename_button = QPushButton("Rename")
        self.cancel_button = QPushButton("Cancel")

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.rename_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        self.rename_button.clicked.connect(self.rename)
        self.cancel_button.clicked.connect(self.reject)

    def rename(self):
        new_name = self.line_edit.text()
        if new_name:
            self.accept()
            self.new_name = new_name
        else:
            self.reject()