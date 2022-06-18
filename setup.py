from importlib_metadata import requires
from setuptools import find_packages, setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Abhirami Kumaraguruparan"
PACKAGES= ["housing"]
REQUIREMENT_FILENAME = "requirements.txt"

def get_requirements_list()->List[str]: # -> List[str] notation means resturn list of str
    """
    Description : This function s going to return list of requirements
    metioned in requirements.txt

    return : This function is going to 
    return a list contain names of libraries in requirements.txt file
    """
    
    
    with open(REQUIREMENT_FILENAME) as req_file:
        return req_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author=AUTHOR,
    description= "This is my first ML project",
    packages=find_packages(), # This gets all the packages from the project
    install_requires = get_requirements_list()
)
