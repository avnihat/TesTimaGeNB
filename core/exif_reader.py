from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_exif_metadata(image_path):
    image = Image.open(image_path)
    exif_data = {}
    if hasattr(image, '_getexif'):
        exif_raw = image._getexif()
        if exif_raw:
            for tag_id, value in exif_raw.items():
                tag = TAGS.get(tag_id, tag_id)
                exif_data[tag] = value
    return exif_data
