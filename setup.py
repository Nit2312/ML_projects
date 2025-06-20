from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    """ This function will return the list of requirements"""
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements=[req.replace("\n", " ")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="1.0.0",
    author='Nit Patel',
    author_email='Nehnit40@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)

