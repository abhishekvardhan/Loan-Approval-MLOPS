from setuptools import find_packages,setup
from typing import List

setup(
    name='loan_approv',
    version='0.0.1',
    author='Abhisek Vardhan',
    author_email='abhivsp10@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)