from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'assets/logo.icns',
    'packages': [
        'PyQt5',
        'opencv-python',
        'Pillow',
        'imagehash',
        'qrcode',
        'reportlab',
        'tensorflow',
        'keras',
        'exifread'
    ]
}

setup(
    app=APP,
    name='TesTimaGeNB',
    data_files=[('assets', ['assets/logo.icns', 'assets/watermark.png'])],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
