from setuptools import find_packages, setup
from typing import List

REQUIRMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(REQUIRMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requriment_name.replace("\n", "") for requriment_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list


setup(name = "cost_prediction",
      version = "0.0.1",
      descriptions = "Data Science projects",
      author = "Roma",
      author_email = "roma.bhavikatti93@gmail.com",
      packages = find_packages(),
      install_requires =get_requirements() ,
          )