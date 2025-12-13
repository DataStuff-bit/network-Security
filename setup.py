from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirement_list: List[str] = []
    try:
        with open('requirements.txt') as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="network-security",
    version="0.0.1",
    author="Shrey Shukla",
    author_email="shrshukla2567@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
