from setuptools import setup, Extension
import os
import subprocess

# Get the absolute path of the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Set the path to the chromaprint source directory
chromaprint_dir = os.path.join(current_dir, ".")

# Run the necessary commands
subprocess.run(["cmake", "-DCMAKE_BUILD_TYPE=Release", "-DBUILD_TOOLS=ON", "."], cwd=chromaprint_dir)
subprocess.run(["make"], cwd=chromaprint_dir)
subprocess.run(["make", "install"], cwd=chromaprint_dir)

# Create symbolic links
subprocess.run(["rm", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1.5.0"])
subprocess.run(["rm", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1"])
subprocess.run(["ln", "-s", "/usr/local/lib/libchromaprint.so.1.5.0", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1.5.0"])
subprocess.run(["ln", "-s", "/usr/local/lib/libchromaprint.so.1", "/usr/lib/x86_64-linux-gnu/libchromaprint.so.1"])

# Define the extension module
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
