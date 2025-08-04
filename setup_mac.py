from setuptools import setup

APP = ['main.py']  # Uygulamanın giriş noktası
DATA_FILES = []    # Dahil etmek istediğin ekstra dosyalar varsa buraya ekle
OPTIONS = {
    'argv_emulation': True,
    'packages': ['cv2'],  # opencv-python modülü
    'iconfile': None      # Eğer .icns simgen varsa burada tanımlayabilirsin
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
