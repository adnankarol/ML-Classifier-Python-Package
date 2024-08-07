__author__ = "Adnan Karol"
__version__ = "1.1.1"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "PROD"

# Import Dependencies
from setuptools import setup, find_packages

# Read the long description from the README file
with open("README.md", "r") as file:
    long_description = file.read()

# Read dependencies from requirements.txt
def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

setup(
    name='classifierAgent',
    version='1.1.1',
    description='A Python package for performing classification on datasets.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/adnankarol/classifierAgent',
    author='Adnan Karol',
    author_email='adnanmushtaq5@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        'machine learning', 'classification', 'random forest', 'xgboost', 
        'svm', 'logistic regression', 'naive bayes', 'knn', 'decision tree'
    ],
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'classifierAgent=classifierAgent:classifierAgent', 
        ],
    },
)
