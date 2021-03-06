from setuptools import setup, Extension
from os import path
from io import open

## TEST INSTALL = pip install --index-url https://test.pypi.org/simple/ neoscrypt

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


neoscrypt_module = Extension('neoscrypt',
                             sources=['src/neoscryptmodule.c',
                                      'src/neoscrypt.c'],
                             include_dirs=['.', 'src'])

setup(name='neoscrypt',
      version='1.2.4',
      description='Bindings for the NeoScrypt proof-of-work algorithm',
      author='John Doering',
      author_email='ghostlander@phoenixcoin.org',
      url='https://github.com/ghostlander/NeoScrypt ',
      ext_modules=[neoscrypt_module],
      zip_safe=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      )
