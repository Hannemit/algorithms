from setuptools import find_packages, setup

setup(
    name='algorithms',
    packages=find_packages(),
    version='0.1.0',
    description='A collection of algorithms',
    author='Hanne',
    license='MIT',
    install_requires=[
        'numpy>=1.17.4',
        'pytest',
        'pre-commit'
    ]
)