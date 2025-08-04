import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from gui.interface import TesTimaGeNBWindow

def check_model_file():
    model_path = "models/gan_detector_resnet.h5"
    if not os.path.exists(model_path):
        return False, model_path
    return True, model_path

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model_ok, model_path = check_model_file()
    if not model_ok:
        QMessageBox.critical(None, "Model Dosyası Eksik",
            f"Gerekli GAN modeli bulunamadı:\n{model_path}\n\nLütfen 'models' klasörüne doğru dosyayı ekleyin.")
        sys.exit(1)

    window = TesTimaGeNBWindow()
    window.show()
    sys.exit(app.exec_())
