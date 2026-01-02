'''
The setup.py file is an essential part of packaging and distruvuting python projects. It us used by setuptools(or distutils in older Python versions to defince the configuration of your projext, such as its metadata, dependencies, and more)
'''

from setuptools import find_packages, setup
from typing import List 

def get_requirements()->List[str]:
    """

        This function returns the list of requirements

    """
    requirement_lst:List[str]=[]
    try:
        with open ('requirements.txt','r') as file:
            # REad lines from file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                    
                    
    except FileNotFoundError:
        print("Requirements.txt file is not found")
    
    return requirement_lst

print(get_requirements())         


setup(
    name="Network_Security",
    version="0.0.1",
    author="Jai Singh",
    author_email="nooneavalon@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)           