from setuptools import setup


def readme():
    with open('README.md') as file:
        _readme = file.read()

    return _readme


def requirements():
    with open('requirements.txt') as file:
        _requirements = file.read().splitlines()

    return _requirements


setup(
    name='epic_games_free',
    version='0.1.0',
    author='LINER999',
    author_email='contact.liner999@gmail.com',
    description='An Epic Games Store free games API wrapper',
    long_description=readme(),
    license='MIT',
    packages=['epic_games_free'],
    url='https://github.com/r-liner/epic_games_free/',
    package_data={'epic_free_games': ["VERSION"]},
    include_package_data=True,
    requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
