"""Setup Baird"""
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    README = f.read()

setup(
    name='baird',
    version='0.1.0',
    description='A tool for connecting to and working on multiple servers over SSH using TMUX',
    long_description=README,
    author='Boweevil',
    author_email='argonaut.linux@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'libtmux',
    ],
    entry_points={
        'console_scripts': [
            'baird=baird.main:main'
        ]
    }
)
