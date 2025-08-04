from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5', 'cv2', 'tensorflow', 'PIL', 'numpy', 'imagehash', 'exifread'],
}

setup(
    app=APP,
    name='TesTimaGeNB',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
