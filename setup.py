import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="screenshots",
    version="0.0.2.dev3",
    author="chincheta",
    author_email="dev@chincheta.com",
    description="Python library to make screenshots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chincheta/screenshots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'selenium==3.141.0',
        'Pillow==7.1.2',
        'tweepy==3.8.0'
    ],
    python_requires='>=3.6',
)
