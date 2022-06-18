from setuptools import find_packages, setup
from typing import List


#declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Shivam Singh"
DESCRIPTION ="This is my first FSDS machine learnig project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mention in requirements.txt

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
instal_requires=get_requirements_list()
)
  