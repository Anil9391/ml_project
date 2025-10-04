from setuptools import find_packages, setup
from typing import List
import os

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements.txt and return a list of dependencies
    """
    requirements = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            requirements = f.readlines()
        # Remove newlines and any editable install markers
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e")]
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Anil',
    author_email='singalanil1995@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.8',
)
