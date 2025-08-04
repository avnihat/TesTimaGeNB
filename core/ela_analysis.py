from PIL import Image, ImageChops, ImageEnhance

def analyze_ela(image_path):
    original = Image.open(image_path).convert('RGB')
    original.save("output/temp_ela.jpg", "JPEG", quality=90)
    compressed = Image.open("output/temp_ela.jpg")

    diff = ImageChops.difference(original, compressed)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])

    scale = 255.0 / max_diff if max_diff != 0 else 1
    ela_image = ImageEnhance.Brightness(diff).enhance(scale)
    ela_image.save("output/ela_result.jpg")

    return "output/ela_result.jpg"
