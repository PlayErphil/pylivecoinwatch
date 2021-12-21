from setuptools import setup, find_packages

setup(
    name='pylivecoinwatch',
    version='1.0.0',
    license='MIT',
    description='Python wrapper around the CoinGecko API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Rene Gonzalez',
    url='https://github.com/PlayErphil/LCW-API-Wrapper',

    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)