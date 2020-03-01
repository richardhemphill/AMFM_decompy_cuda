# -*- coding: utf-8 -*-

import io
from setuptools import setup

try:
    long_description = io.open('README.md',encoding='utf8').read()
except:
    long_description ='Package containing the tools necessary for decomposing a \
            speech signal into its modulated components, aka AM-FM decomposition.'

setup(
    name = 'AMFM_decompy_cuda',
    version = '0.0.0',
    author = 'Richard Hemphill',
    author_email = 'richardlhemphill@gmail.com',
    packages = ['amfm_decompy_cuda'],
    scripts = ['bin/AMFM_test.py'],
    package_data = {'amfm_decompy_cuda': ['*.wav']},
    install_requires = ['numpy', 'scipy',],
    url = 'https://github.com/richardhemphill/AMFM_decompy_cuda/',
    license = 'LICENSE.txt',
    description = 'Package containing the tools necessary for decomposing a \
speech signal into its modulated components, aka AM-FM decomposition.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers = [
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.5',
                'Topic :: Scientific/Engineering',
                'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                'Topic :: Scientific/Engineering :: Information Analysis',
                'Topic :: Software Development :: Libraries :: Python Modules',
                ],
    keywords = 'Python, speech, pitch, QHM, YAAPT, modulated components, \
                AM-FM decomposition',
    zip_safe = False,
    include_package_data = True,
)
