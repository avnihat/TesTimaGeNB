try:
    import tensorflow as tf
except ImportError:
    tf = None

def analyze_ela(image_path):
    if tf is None:
        raise ImportError("TensorFlow yüklü değil. Lütfen 'requirements.txt' dosyasına ekleyerek yükleyin.")
    
    # Buraya model analiz kodları gelecek
    pass
