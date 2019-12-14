# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:21:16 2019

@author: Guest Group
"""

from setuptools import setup

setup(
      name = 'free_properties',
      packages = ['free_properties'],
      license='MIT',
      version = '0.2.2',
      description = 'Manage properties outside a class',
      long_description=open('README.rst').read(),
      author = 'Yoel Cortes-Pena',
      install_requires=[],
      package_data = {'free_properties': []},
      platforms=["Windows"],
      author_email = 'yoelcortes@gmail.com',
      url = 'https://github.com/yoelcortes/free_properties',
      download_url = 'https://github.com/yoelcortes/free_properties.git'
      )
      
