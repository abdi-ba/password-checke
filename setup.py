from setuptools import setup

setup(
    name="abdi-check",
    version="1.0",
    py_modules=["abdi"],  # This MUST match the filename abdi.py
    entry_points={
        'console_scripts': [
            'abdi-check = abdi:main', # This links the command to the main() function
        ],
    },
)
