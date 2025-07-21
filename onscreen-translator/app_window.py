from PyQt6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget, QLabel, QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt, QThreadPool, QTimer
from PIL import ImageGrab
from selection import SelectionWindow
from worker import TranslationWorker

class ScreenTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screen Translator")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        
        self.selection_window = None
        self.threadpool = QThreadPool()

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.translate_area_btn = QPushButton("terjemahkan Area")
        self.translate_full_btn = QPushButton("terjemahkan seluruh layar")
        button_layout.addWidget(self.translate_area_btn)
        button_layout.addWidget(self.translate_full_btn)
        
        self.status_label = QLabel("pilih mode terjemahan...")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.result_text)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.translate_area_btn.clicked.connect(self.start_area_translation)
        self.translate_full_btn.clicked.connect(self.start_full_screen_translation)

    def start_area_translation(self):
        self.hide()
        self.selection_window = SelectionWindow()
        self.selection_window.area_selected.connect(self.capture_and_process)
        self.selection_window.show()

    def start_full_screen_translation(self):
        self.hide()
        QTimer.singleShot(200, lambda: self.capture_and_process())

    def capture_and_process(self, rect=None):
        if rect:
            bbox = (rect.x(), rect.y(), rect.x() + rect.width(), rect.y() + rect.height())
            screenshot = ImageGrab.grab(bbox=bbox)
        else:
            screenshot = ImageGrab.grab()

        self.show()
        self.status_label.setText("memprses...")
        self.result_text.clear()
        
        worker = TranslationWorker(image=screenshot)
        worker.signals.result.connect(self.display_result)
        worker.signals.progress.connect(self.update_status)
        worker.signals.error.connect(self.display_error)
        
        self.threadpool.start(worker)

    def update_status(self, message):
        self.status_label.setText(message)

    def display_result(self, text):
        self.result_text.setText(text)

    def display_error(self, error_tuple):
        _, error_message = error_tuple
        QMessageBox.critical(self, "error", f"terjadi kesalahan:\n{error_message}")
        self.update_status("terjadi kesalahan!")

