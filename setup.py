from setuptools import setup, find_packages

setup(
    name='sqlmodel',
    version='1.0.0',
    url='https://github.com/javivdm/sqlmodel.git',
    packages=find_packages(),
    install_requires=['SQLAlchemy >=1.4.17, <1.5.0', 'pydantic >=1.8.2, <2.0.0'],
)
