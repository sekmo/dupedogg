from setuptools import setup

setup(
    name="dupedogg",
    version="0.1.1",
    py_modules=["dupedogg"],
    install_requires=[
        "Pillow",
        "ImageHash",
        "tqdm",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "dupedogg = dupedogg:main",
        ],
    },
)
