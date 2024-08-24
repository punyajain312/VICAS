import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QDesktopWidget, QHBoxLayout, QScrollArea, QMenu, QAction, QInputDialog, QDialog, QLineEdit,QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from rename_dialog import RenameDialog
from inspection_form import InspectionForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get screen dimensions
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Set up the main window
        self.setWindowTitle("VICAS")
        self.setGeometry(
            int(screen_width * 0.125),
            int(screen_height * 0.125),
            int(screen_width * 0.75),
            int(screen_height * 0.75)
        )

        # Create content sections
        self.left_section = self.create_left_section()
        self.right_section = self.create_right_section()

        # Layout for sections
        sections_layout = QHBoxLayout()
        sections_layout.addWidget(self.left_section, 2)  # 40% width
        sections_layout.addWidget(self.right_section, 3)  # 60% width
        sections_layout.setContentsMargins(0, 0, 0, 0)
        sections_layout.setSpacing(0)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.create_header())  # Add header
        main_layout.addLayout(sections_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_left_section(self):
        """Create the left section with a 'History' heading and history files."""
        left_section = QWidget()
        left_section.setStyleSheet("background-color:#252525;  outline: none;")
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(35, 35, 35, 35)  # Add some padding to the main left section layout
        left_layout.setSpacing(10)

        # History section heading
        history_heading = QLabel("History")
        history_heading.setAlignment(Qt.AlignCenter)  # Center the text
        history_heading.setStyleSheet("color: #ffcc21; font-size: 28px; font-weight: bold; padding: 10px;  outline: none;")
        left_layout.addWidget(history_heading)

        # Create a container widget for the history files layout
        history_container = QWidget()

        history_files_layout = QVBoxLayout()
        history_files_layout.setSpacing(10)  # Spacing between the files
        history_files_layout.setContentsMargins(15, 10, 15, 10)  # Add padding inside the layout

        # Add files to the history files layout
        history_files = [f"File{i}.txt" for i in range(1, 25)]  # 25 files for scrollability

        for file_name in history_files:
            file_label = QLabel(file_name)
            file_label.setStyleSheet("color: white; padding: 25px; border: 2px solid #ffcc21; border-radius: 10px; outline: none;")  # Padding for each file label
            file_label.setCursor(Qt.PointingHandCursor)  # Change cursor to pointer
            file_label.mousePressEvent = lambda event, fname=file_name: self.file_clicked(event, fname)  # Connect click event
            file_label.setContextMenuPolicy(Qt.CustomContextMenu)  # Enable custom context menu
            file_label.customContextMenuRequested.connect(self.show_context_menu)  # Connect right-click to context menu
            history_files_layout.addWidget(file_label)

        history_container.setLayout(history_files_layout)

        # Scroll area for history files
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(history_container)

        # Custom scrollbar style
        scroll_area.setStyleSheet("""
        QScrollArea {
            border: none;  /* Remove any border from the scroll area */
            background-color: #333;
        }
        
        QScrollBar:vertical {
            border: none;
            background: #333;
            width: 10px;
            margin: 15px 0 15px 0;  /* Top and bottom padding */
        }

        QScrollBar::handle:vertical {
            background: red;  /* Red scrollbar handle */
            min-height: 20px;
            border-radius: 5px;
            border: none;  /* Remove any border */
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """)

        # Add the scroll area to the left layout
        left_layout.addWidget(scroll_area)

        left_section.setLayout(left_layout)
        return left_section

    def create_right_section(self):
        """Create the right section with initial home page."""
        self.right_section = QWidget()
        self.right_layout = QVBoxLayout()

        # Initial "VICAS" label with updated styling
        self.home_label = QLabel("VICAS")
        self.home_label.setStyleSheet("""
            QLabel {
                font-size: 72px;
                font-weight: bold;
                color: #ffcc21;
            }
        """)

        self.home_label.setAlignment(Qt.AlignCenter)  # Center the text in the label
        self.right_layout.addWidget(self.home_label, alignment=Qt.AlignCenter)

        # "New Inspect" button
        self.new_inspect_button = QPushButton("New Inspect")
        self.new_inspect_button.setStyleSheet("""
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
        self.new_inspect_button.setFixedWidth(150)
        self.new_inspect_button.clicked.connect(self.show_inspection_form)
        self.right_layout.addWidget(self.new_inspect_button, alignment=Qt.AlignCenter)

        # Create the label for displaying file content
        self.right_label = QLabel("")
        self.right_label.setStyleSheet("font-size: 20px; color: #ffcc21;")
        self.right_label.hide()  # Hide it initially

        self.right_layout.setContentsMargins(20, 20, 20, 20)
        self.right_layout.setSpacing(10)
        self.right_layout.addStretch()  # Push everything to the top

        self.right_section.setLayout(self.right_layout)
        return self.right_section

    def file_clicked(self, event, file_name):
        """Handle the file click event."""
        # Remove the initial home widgets
        self.home_label.hide()
        self.new_inspect_button.hide()

        # Display the clicked file's content in the right section
        self.right_label.setText(f"Content of {file_name}")
        self.right_layout.addWidget(self.right_label, alignment=Qt.AlignTop)

    def show_context_menu(self, pos):   
        """Show context menu on right-click."""
        sender = self.sender()
        file_name = sender.text()

        context_menu = QMenu(self)
        context_menu.setStyleSheet("""
        QMenu {
            background-color: #333;
            color: #ffcc21;
            border: 1px solid #ffcc21;
            border-radius: 5px;
        }
        QMenu::item {
            padding: 5px 10px;
        }
        QMenu::item:selected {
            background-color: #555;
        }
        """)

        open_action = QAction("Open", self)
        open_action.triggered.connect(lambda: self.open_file(file_name))

        rename_action = QAction("Rename", self)
        rename_action.triggered.connect(lambda: self.rename_file(sender))

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(lambda: self.delete_file(sender))

        context_menu.addAction(open_action)
        context_menu.addAction(rename_action)
        context_menu.addAction(delete_action)

        context_menu.exec_(sender.mapToGlobal(pos))

    def open_file(self, file_name):
        """Open the file (simulate opening for now)."""
        self.right_label.setText(f"Opened {file_name}")

    def rename_file(self, file_label):
        """Rename the file."""
        old_name = file_label.text()
        dialog = RenameDialog(old_name, self)
        if dialog.exec_():
            new_name = dialog.new_name
            file_label.setText(new_name)
            self.right_label.setText(f"Renamed {old_name} to {new_name}")

    def delete_file(self, file_label):
        """Delete the file."""
        file_name = file_label.text()
        file_label.deleteLater()
        self.right_label.setText(f"Deleted {file_name}")
       
    def resizeEvent(self, event):
        super().resizeEvent(event)  # Call the base class resizeEvent method

    def create_header(self):
        """Create the header/navbar."""
        header = QWidget()
        header.setStyleSheet("background-color: #000; color: #ffcc21;")
        header_layout = QHBoxLayout()

        # Remove default margins and spacing
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)

        # Header logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("./assets/img/logo.jpg")  # Replace with the path to your logo file
        logo_label.setPixmap(logo_pixmap.scaled(200, 100, Qt.KeepAspectRatio))  # Scale the image
        logo_label.setStyleSheet("padding: 10px; padding-top: 13px; padding-left: 13px;")  # Add padding to the QLabel
        header_layout.addWidget(logo_label)

        # Navigation buttons
        self.home_button = QPushButton("Home")
        self.about_button = QPushButton("About")
        self.contact_button = QPushButton("Contact")
        
        # Add a spacer to push the buttons to the right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header_layout.addWidget(spacer)

        header_layout.addWidget(self.home_button)
        header_layout.addWidget(self.about_button)
        header_layout.addWidget(self.contact_button)

        # Apply styles to navigation buttons
        for button in [self.home_button, self.about_button, self.contact_button]:
            button.setStyleSheet("""
                font-size: 22px;
                font-weight: bold; 
                padding: 10px 30px; 
                background-color: #000; 
                color: #ffcc21;
            """)

        # Search button with icon
        self.search_button = QPushButton()
        self.search_button.setStyleSheet("padding: 5px; border: none;")
        search_pixmap = QPixmap("./assets/img/search.jpg")  # Replace with the path to your search icon file
        search_pixmap = search_pixmap.scaled(100, 30, Qt.KeepAspectRatio)  # Scale the image to make it smaller
        search_icon = QIcon(search_pixmap)  # Convert QPixmap to QIcon
        self.search_button.setIcon(search_icon)
        self.search_button.setIconSize(search_pixmap.size())  # Ensure the button uses the scaled icon size
        self.search_button.clicked.connect(self.open_search_input)
        header_layout.addWidget(self.search_button)

        # Set header layout and height
        header.setLayout(header_layout)
        header_height = int(QDesktopWidget().screenGeometry().height() * 0.1)
        header.setFixedHeight(header_height)

        return header

    def open_search_input(self):
        text, ok = QInputDialog.getText(self, "Search History", "Enter search term:")
        if ok and text:
            self.search_history_files(text)

    def search_history_files(self, search_term):
        for i in range(self.left_section.layout().count()):
            widget = self.left_section.layout().itemAt(i).widget()
            if isinstance(widget, QLabel) and search_term.lower() in widget.text().lower():
                widget.setStyleSheet("color: yellow; background-color: #444; padding: 25px; border: 2px solid #ffcc21; border-radius: 10px; outline: none;")  # Highlight found files
            else:
                widget.setStyleSheet("color: white; padding: 25px; border: 2px solid #ffcc21; border-radius: 10px; outline: none;") # Reset others

    def show_inspection_form(self):
        """Display the inspection form in the right section."""
        self.home_label.hide()
        self.new_inspect_button.hide()

        # Create and show the inspection form
        self.inspection_form = InspectionForm()
        self.right_layout.addWidget(self.inspection_form)
        self.inspection_form.show()

    def show_home_page(self):
        # Show the home page and hide inspection form
        self.home_label.show()
        self.new_inspect_button.show()
        self.right_label.hide()
        if hasattr(self, 'inspection_form'):
            self.inspection_form.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 