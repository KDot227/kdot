from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A anti skid package"
LONG_DESCRIPTION = (
    "A package that makes it easy to add anti skid to all of your (my) repos"
)

setup(
    name="kdot",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="kdot227",
    author_email="suckmaballs@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords="kdot",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
