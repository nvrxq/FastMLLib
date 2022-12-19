#!/usr/bin/env python3
# encoding: utf-8


from setuptools import setup, Extension

module = Extension('LinAlgLib_C', include_dirs = ['/usr/local/include'],
                    library_dirs = ['/usr/lib/python3/dist-packages'], sources = ['FastML_C/LinAlg_C.c'])

setup(name='FastMLLib',
      version='1.1.0',
      description='Machine Learning Library',
      ext_modules=[module])
