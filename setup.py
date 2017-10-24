from setuptools import setup, find_packages
setup(
    name="stattleship",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['requests>=2.18.4', 'pandas>=0.20.3'],
    author="Scotty Pate",
    author_email="scottypate@me.com",
    description="Python wrapper for Stattleship API",
    url="http://github.com/scottypate/stattleship.git"
)