def analyze_gps_location(exif_data):
    gps = exif_data.get('GPSInfo', None)
    software = exif_data.get('Software', '')
    if gps and ("Photoshop" in software or "Snapseed" in software):
        return "⚠️ GPS ile yazılım uyuşmazlığı tespit edildi"
    return "✅ GPS & Yazılım uyumu sağlandı"
