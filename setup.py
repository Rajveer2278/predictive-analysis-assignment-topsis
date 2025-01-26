from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis_Rajveer_102203195",
    version="1.0.14",
    author="Rajveer Singh",
    author_email="rsingh3_be22@thapar.com",
    description="A python package for implementing topsis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["Topsis_Rajveer_102203195 = Topsis_Rajveer_102203195.topsis:main"]},
)
