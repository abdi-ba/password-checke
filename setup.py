from setuptools import setup

setup(
    name="abdi-check",
    version="1.0",
    py_modules=["abdi"],  
    entry_points={
        'console_scripts': [
            'abdi-check=abdi:main', 
        ],
    },
)
