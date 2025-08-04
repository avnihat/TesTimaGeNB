from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from datetime import datetime

def generate_pdf_report(image_path, results, output_pdf_path, language="TR", watermark_path=None):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    width, height = A4
    c.setFont("Times-Roman", 11)

    if watermark_path:
        watermark = ImageReader(watermark_path)
        c.drawImage(watermark, 100, 300, width=400, mask='auto', preserveAspectRatio=True)

    c.drawString(50, 800, "TesTimaGeNB Otomatik Raporu - Av. Nihat BAŞ")
    c.drawString(50, 785, f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = 750
    for key, value in results.items():
        c.setFont("Times-Bold", 11)
        c.drawString(50, y, str(key) + ":")
        c.setFont("Times-Roman", 11)
        if isinstance(value, dict):
            for subk, subv in value.items():
                y -= 15
                c.drawString(70, y, f"- {subk}: {subv}")
        else:
            y -= 15
            c.drawString(70, y, str(value))
        y -= 30

    c.drawImage(image_path, 400, 600, width=150, preserveAspectRatio=True, mask='auto')
    if "qr_code" in results.get("Hash Bilgisi", {}):
        c.drawImage(results["Hash Bilgisi"]["qr_code"], 400, 450, width=100, mask='auto')

    c.save()
