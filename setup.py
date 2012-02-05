from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='finpypa',
      version=version,
      description="Financial papers or products",
      long_description="""Financial papers or products""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='finance',
      author='Miguel Vaz',
      author_email='migueljvaz@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
