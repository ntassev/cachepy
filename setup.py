from setuptools import setup, find_packages

setup(
   name='cachepy',
   version='1.0.0',
   url='https://github.com/ntassev/cachepy',
   author='Juan Pablo Guereca',
   description='Module which implements a per GAE instance data cache, '
               'similar to what you can achieve with APC in PHP instances.',
   packages=find_packages(),
)
