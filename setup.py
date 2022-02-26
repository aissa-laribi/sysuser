# This will call the setuptools module, then import the setup and find_packages
# functions from it
from setuptools import setup, find_packages
#This will read the package description from our README.rst file
with open('README.rst', encoding='UTF-8') as f:
  readme = f.read()
# This will actually do the calling out to setup, and set some of the information
# This will actually do the calling out to setup, and set some of the information
# about the package itself
setup(
  name='sysuser' ,
  version='1.0.0',
  description='Command line user export utility',
  long_description=readme,
  author='Your Name',
  author_email='aissalaribi@yahoo.fr',
  # This will define where to look for the package itself.
  # We're pointing find_packages at local src directory
  packages=find_packages('src'),
  package_dir={'': 'src'},
  install_requires=[],
  entry_points={
        'console_scripts': 'sysuser=sysuser.cli:main'
    }
)
