from PyQt6.QtCore import QObject, pyqtSignal, QRunnable
from PIL import ImageGrab
import pytesseract
from googletrans import Translator, LANGUAGES
from config import TESSERACT_CMD_PATH

if TESSERACT_CMD_PATH:
    try:
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD_PATH
    except Exception as e:
        print(f"error: tidak dapat megatur path tesseract: {e}")

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(str)
    progress = pyqtSignal(str)


class TranslationWorker(QRunnable):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.signals = WorkerSignals()

    def run(self):
        try:
            self.signals.progress.emit("1/3: mengekstrak teks...")
            extracted_text = pytesseract.image_to_string(self.image, lang='eng+ind')
            if not extracted_text.strip():
                self.signals.progress.emit("tidak ada teks yang terdeteksi")
                self.signals.finished.emit()
                return

            self.signals.progress.emit("2/3: menerjemahkan teks...")
            translator = Translator()
            translated = translator.translate(extracted_text, dest='id')

            self.signals.progress.emit("3/3: selesai")
            source_lang = LANGUAGES.get(translated.src, translated.src)
            result_str = f"bahasa asli: {source_lang.title()}\n"
            result_str += f"--------------------------------\n"
            result_str += f"{translated.text}"
            self.signals.result.emit(result_str)

        except Exception as e:
            self.signals.error.emit((type(e), str(e)))
        finally:
            self.signals.finished.emit()

