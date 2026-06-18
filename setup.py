from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list:
    '''
    This function will return the list of requirements
    '''
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name="Ml Project",  
    version="0.1.0",
    Author="Atharva Mapari",
    author_email="atharvamapari13@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)