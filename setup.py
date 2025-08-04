from setuptools import setup, find_packages

setup(
    name='TesTimaGeNB',
    version='1.0.0',
    description='Görsellerin gerçeklik analizini yapan adli yazılım',
    author='Senin Adın',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'opencv-python',
        'Pillow',
        'imagehash',
        'qrcode',
        'reportlab',
        'tensorflow',
        'keras',
        'exifread'
    ],
    entry_points={
        'console_scripts': [
            'testimagenb = main:main'
        ]
    },
    include_package_data=True,
)
