from setuptools import setup

APP = ['main.py']  # Ana dosya
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,  # MacOS argümanlarını terminalsiz çalıştırmak için
    'packages': [
        'PyQt5',
        'cv2',
        'tensorflow',
        'PIL',
        'numpy',
        'imagehash',
        'exifread'
    ],
    'includes': [
        'os',
        'sys',
        'threading',
        'importlib',
    ],
    'iconfile': 'assets/logo.icns',  # (isteğe bağlı) .app için ikon
    'plist': {
        'CFBundleName': 'TesTimaGeNB',
        'CFBundleDisplayName': 'TesTimaGeNB',
        'CFBundleIdentifier': 'com.yourdomain.testimagenb',
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
    }
}

setup(
    app=APP,
    name='TesTimaGeNB',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
