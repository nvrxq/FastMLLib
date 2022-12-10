#!/usr/bin/env python3
# encoding: utf-8


from setuptools import setup, Extension

hello_module = Extension('LinAlgLib_C', include_dirs = ['/usr/local/include'],
                    library_dirs = ['/usr/lib/python3/dist-packages'], sources = ['array/LinAlg_C.c'])

setup(name='hello',
      version='0.1.0',
      description='Hello world module written in C',
      ext_modules=[hello_module])
