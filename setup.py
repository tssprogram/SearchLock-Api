from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()


setup(
    name = "searchlock.py",
    version = "1.0",
    url = "iotiohjgt",
    license = "MIT",
    author = "Mister West",
    author_email = "mrwest@ctemplar.com",
    description = "Biblioteca python para interação da api do painel Searchlock",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        'searchlock',
        'mister-west',
        'painel',
        'python3',
        'python3.x',
        'api'
    ],

    install_requires = [
        'setuptools',
        'requests'
    ],

    setup_requires = [
        "wheel"
    ],
    
    packages = find_packages()
)