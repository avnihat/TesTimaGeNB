import os
import threading
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QHBoxLayout, QMessageBox, QProgressBar,
    QSlider, QComboBox, QTextEdit
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from core.ai_detector import analyze_image_ai
from core.ela_analysis import analyze_ela
from core.exif_reader import extract_exif_metadata
from core.hash_utils import generate_image_hashes
from core.face_detector import detect_faces
from core.gps_checker import analyze_gps_location
from core.resnet_gan_model import analyze_gan_resnet
from core.report_generator import generate_pdf_report

class TesTimaGeNBWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TesTimaGeNB - Görsel Gerçeklik Analizi")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("assets/logo.icns"))
        self.selected_image_path = None
        self.result_summary = {}
        self.language = "TR"
        self.init_ui()
    def init_ui(self):
        layout = QVBoxLayout()

        # Görsel Önizleme
        self.image_label = QLabel("🔍 Henüz bir görsel seçilmedi")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid gray; padding: 10px;")
        layout.addWidget(self.image_label)

        # Görsel Seçme Butonu
        select_button = QPushButton("📁 Görsel Seç")
        select_button.clicked.connect(self.select_image)
        layout.addWidget(select_button)

        # Klasör Seçme Butonu
        folder_button = QPushButton("📂 Klasör Seç")
        folder_button.clicked.connect(self.select_folder)
        layout.addWidget(folder_button)

        # Skor Eşiği Slider
        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setMinimum(50)
        self.threshold_slider.setMaximum(100)
        self.threshold_slider.setValue(80)
        self.threshold_slider.setTickInterval(5)
        layout.addWidget(QLabel("🎚️ Skor Eşiği Ayarı"))
        layout.addWidget(self.threshold_slider)

        # Analizi Başlat Butonu
        analyze_button = QPushButton("🔍 Analizi Başlat")
        analyze_button.clicked.connect(self.start_analysis)
        layout.addWidget(analyze_button)

        # PDF Raporu Butonu
        pdf_button = QPushButton("📝 PDF Raporu Oluştur")
        pdf_button.clicked.connect(self.generate_report)
        layout.addWidget(pdf_button)

        # Dil Seçimi
        self.language_combo = QComboBox()
        self.language_combo.addItems(["Türkçe", "English"])
        self.language_combo.currentIndexChanged.connect(self.change_language)
        layout.addWidget(QLabel("🌐 Dil Seçimi"))
        layout.addWidget(self.language_combo)

        # Sonuçları Gösteren Metin Kutusu
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Görsel Seç",
            "",
            "Tüm Dosyalar (*.png *.jpg *.jpeg *.bmp *.webp *.tiff *.gif *.pdf)"
        )
        if file_path:
            self.selected_image_path = file_path
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
                self.result_box.append("📸 Görsel yüklendi: " + os.path.basename(file_path))
            else:
                self.result_box.append("⚠️ Görsel yüklenemedi. Format desteklenmiyor.")

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Klasör Seç")
        if folder_path:
            self.result_box.append("📂 Klasör seçildi: " + folder_path)
            image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp", ".gif", ".pdf")
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.lower().endswith(image_extensions):
                        full_path = os.path.join(root, file)
                        self.result_box.append(f"📎 Görsel bulundu: {file}")
            self.result_box.append("✅ Taramaya hazır.")

    def start_analysis(self):
        if not self.selected_image_path:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce bir görsel seçin.")
            return

        self.result_box.append("🔎 Analiz başlatılıyor...")
        self.result_summary.clear()
        threshold = self.threshold_slider.value()

        # Analizleri ayrı bir thread'de çalıştır
        thread = threading.Thread(target=self.run_analysis_pipeline, args=(threshold,))
        thread.start()

    def run_analysis_pipeline(self, threshold):
        image_path = self.selected_image_path

        # AI / GAN Tespiti
        ai_score = analyze_image_ai(image_path)
        self.result_summary["AI Skoru"] = ai_score
        self.result_box.append(f"🤖 AI Tespiti Skoru: {ai_score}%")

        # GAN Özel ResNet Tespiti
        gan_score = analyze_gan_resnet(image_path)
        self.result_summary["GAN Tespiti"] = gan_score
        self.result_box.append(f"🧠 GAN ResNet Skoru: {gan_score}%")

        # ELA Analizi
        ela_result = analyze_ela(image_path)
        self.result_summary["ELA"] = ela_result
        self.result_box.append("🧪 ELA analizi tamamlandı.")

        # EXIF ve GPS Analizi
        exif_data = extract_exif_metadata(image_path)
        gps_info = analyze_gps_location(exif_data)
        self.result_summary["EXIF"] = exif_data
        self.result_summary["GPS Uyum"] = gps_info
        self.result_box.append("📍 EXIF & GPS analizi tamamlandı.")

        # Hash & QR
        hash_result = generate_image_hashes(image_path)
        self.result_summary["Hash Bilgisi"] = hash_result
        self.result_box.append("🔐 SHA256 ve pHash hesaplandı.")

        # Yüz Tanıma
        face_result = detect_faces(image_path)
        self.result_summary["Yüz Tespiti"] = face_result
        self.result_box.append(f"👤 Yüzler: {face_result}")

        # Skor renk değerlendirme
        if ai_score >= 85:
            status = "✅ Gerçeklik yüksek"
        elif ai_score >= threshold:
            status = "⚠️ Şüpheli"
        else:
            status = "❌ Yapay Görsel Olabilir"

        self.result_summary["Genel Değerlendirme"] = status
        self.result_box.append(f"📌 Sonuç: {status}")
    def generate_report(self):
        if not self.selected_image_path or not self.result_summary:
            QMessageBox.warning(self, "Uyarı", "Önce bir analiz yapmalısınız.")
            return

        output_path = os.path.join("output", "TesTimaGeNB_Rapor.pdf")
        generate_pdf_report(
            image_path=self.selected_image_path,
            results=self.result_summary,
            output_pdf_path=output_path,
            language=self.language,
            watermark_path="assets/watermark.png"
        )

        self.result_box.append("📄 PDF raporu oluşturuldu: " + output_path)
        QMessageBox.information(self, "Rapor", "Rapor başarıyla kaydedildi.")

    def change_language(self, index):
        lang = self.language_combo.currentText()
        if lang == "English":
            self.language = "EN"
            self.setWindowTitle("TesTimaGeNB - Image Authenticity Checker")
            self.result_box.append("🌐 Language switched to English.")
        else:
            self.language = "TR"
            self.setWindowTitle("TesTimaGeNB - Görsel Gerçeklik Analizi")
            self.result_box.append("🌐 Dil Türkçe olarak ayarlandı.")
