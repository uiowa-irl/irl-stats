import setuptools

with open("irl-stats.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="irl",
    version="0.0.1",
    author="John M. Cook",
    author_email="john-cook@uiowa.edu",
    description="A collection of useful statistics packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uiowa-irl/irl-stats.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",        
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)