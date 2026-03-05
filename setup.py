from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''this function will return the list of requirement'''

    requirement= []

    with open (file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n',"") for req in requirement]
    return requirement

setup(name = 'datascienceproject' ,
       version = '0.0.1',
       author='vaish',
       author_email = 'vaishnavighadge18@gmail.com',
       packages = find_packages(),
       install_requires =get_requirement('requirement.txt'))