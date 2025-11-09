import platform
from setuptools import setup, Extension
from Cython.Build import cythonize

# Detect system architecture automatically
arch = platform.architecture()[0]
print(f"\n🔹 Detected Python Architecture: {arch}\n")

# Define Cython extension
extensions = [
    Extension(
        "RAJA_OTP_bypass",
        sources=["RAJA_OTP_bypass.pyx"],  # your main Cython source file
        extra_compile_args=[
            "-O2",  # optimization
            "-Wno-unreachable-code",
            "-Wno-unreachable-code-fallthrough"
        ]
    )
]

# Run setup
setup(
    name=f"RAJA_OTP_bypass-{arch}",
    version="1.0",
    description=f"RAJA_OTP_bypass module compiled for {arch}",
    ext_modules=cythonize(extensions, language_level="3"),
)

print(f"\n✅ Build for {arch} complete!\n")