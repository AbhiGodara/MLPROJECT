from setuptools import find_packages,setup
from typing import List

hyphen_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    #this function will return the list of requirments
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if hyphen_E_DOT in requirments:
            requirments.remove(hyphen_E_DOT)
    return requirments


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='abhishek',
    author_email='abhishekgodara032@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)