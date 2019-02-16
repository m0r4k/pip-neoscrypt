from setuptools import setup, Extension, dist
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class BinaryDistribution(dist.Distribution):
    def is_pure(self):
        return False

neoscrypt_module = Extension('neoscrypt',
                             sources=['src/neoscryptmodule.c',
                                      'src/neoscrypt.c'],
                             include_dirs=['.', 'neoscrypt', 'neoscrypt/lib', 'src'])

setup(name='neoscrypt',
      version='1.2',
      description='Bindings for the NeoScrypt proof-of-work algorithm',
      author='John Doering',
      author_email='ghostlander@phoenixcoin.org',
      url='https://github.com/ghostlander/NeoScrypt ',
      ext_modules=[neoscrypt_module],
      zip_safe=True,
      long_description=long_description,
      long_description_content_type='text/markdown',
      package_data={'neoscrypt': ['lib/neoscrypt.dll','lib/neoscrypt.dylib', 'lib/neoscrypt.so']},
      include_package_data=True,
      distclass=BinaryDistribution,
      packages=['neoscrypt']
      )
