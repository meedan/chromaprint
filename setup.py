from setuptools import setup, Extension

setup(
    name='chromaprint',
    version='1.0.0',
    ext_modules=[
        Extension(
            'chromaprint',
            sources=['src/chromaprint.cpp'],
            include_dirs=['src'],
            libraries=['chromaprint'],
        )
    ]
)
