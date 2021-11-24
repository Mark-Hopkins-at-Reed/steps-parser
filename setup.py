from setuptools import setup, find_packages

setup(name='steps',
      version='1.0',
      packages=find_packages(),
      install_requires=[
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )

