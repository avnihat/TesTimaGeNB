from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'assets/logo.icns',
    'packages': ['PyQt5', 'cv2', 'PIL', 'imagehash', 'qrcode', 'reportlab', 'tensorflow', 'keras']
}

setup(
    app=APP,
    name='TesTimaGeNB',
    data_files=[],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
