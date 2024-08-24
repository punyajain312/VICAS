import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Capture")
        self.image_label = QLabel(self)
        self.capture_btn = QPushButton("Capture", self)
        self.capture_btn.clicked.connect(self.capture_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.capture_btn)
        self.setLayout(layout)

        self.cam = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        ret, frame = self.cam.read()    
        frame = cv2.flip(frame, 1)
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch*w
            convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(convert_to_qt_format))

    def capture_image(self):
        ret, frame = self.cam.read()
        frame = cv2.flip(frame, 1)
        if ret:
            cv2.imwrite("captured_image.png", frame)
            QMessageBox.information(self, "Image Captured", "Image saved as captured_image.png")

    def closeEvent(self, event):
        self.cam.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
