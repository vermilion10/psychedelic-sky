import sys
from PyQt6.QtWidgets import QApplication
from app_window import ScreenTranslatorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ScreenTranslatorApp()
    main_window.show()
    sys.exit(app.exec())

