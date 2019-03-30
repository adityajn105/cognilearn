import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cognilearn",
    version="0.0.3",
    author="Aditya Jain",
    author_email="aditya.jain@cognizant.com",
    description="A set of utilities helpful during analytics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adityajn105",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)