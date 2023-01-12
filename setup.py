from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    Returns list of requirements 
    '''
    requirement_list:List[str] = []
    with open('requirements.txt', 'r') as r:
        content = r.read()

    requirement_list:List[str] = []
    for requirement in content.split('\n'):
        requirement_list.append(requirement)

    return requirement_list    


setup(
    name = 'sensor',
    version = '0.0.1',
    author = 'Saurabh Bhardwaj',
    author_email = 'aryan.saurabhbhardwaj@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)



    