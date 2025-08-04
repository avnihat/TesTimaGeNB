import imagehash
import qrcode
from PIL import Image
import hashlib
import json

def generate_image_hashes(image_path):
    img = Image.open(image_path)
    sha256 = hashlib.sha256(img.tobytes()).hexdigest()
    phash = str(imagehash.phash(img))

    qr = qrcode.make(sha256)
    qr.save("output/qr_code.png")

    try:
        with open("data/phash_db.json", "r") as f:
            db = json.load(f)
    except:
        db = {}

    match = False
    for entry in db.values():
        if entry.get("phash") == phash:
            match = True

    return {
        "sha256": sha256,
        "phash": phash,
        "qr_code": "output/qr_code.png",
        "veri_tabani_eslesme": match
    }
