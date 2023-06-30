from setuptools import setup, Extension
import subprocess

# Run the necessary commands
subprocess.run(["cmake", "-DCMAKE_BUILD_TYPE=Release", "-DBUILD_TOOLS=ON", "./chromaprint"])
subprocess.run(["make"], cwd="./chromaprint")
subprocess.run(["make", "install"], cwd="./chromaprint")

# Create symbolic links
subprocess.run(["rm", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1.5.0"])
subprocess.run(["rm", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1"])
subprocess.run(["ln", "-s", "/usr/local/lib/libchromaprint.so.1.5.0", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1.5.0"])
subprocess.run(["ln", "-s", "/usr/local/lib/libchromaprint.so.1", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1"])


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
