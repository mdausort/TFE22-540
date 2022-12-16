# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:19:19 2022

@author: manou
"""

from setuptools import setup

setup(
    name='alcoholic_tfe22540',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/mdausort/TFE22-540',
    author='Manon Dausort',
    author_email='manon.dausort@uclouvain.be',
    license='BSD 2-clause',
    packages=['tfe22540'],
    install_requires=['numpy',
                      'nibabel',     
                      'xlsxwriter',
                      'time',
                      'math',
                      'pandas',
                      'collections',
                      'os',
                      'matplotlib',
                      'sklearn',
                      'seaborn',
                      'dipy',
                      'mpl_toolkits',
                      'elikopy',
                      'multiprocessing',
                      'itertools',
                      'skimage',
                      'sys',
                      'scipy',
                      'future',
                      'datetime',
                      'subprocess',
                      'openpyxl'
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',    
        'Programming Language :: Python',
    ],
)