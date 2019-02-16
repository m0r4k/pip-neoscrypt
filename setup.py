from setuptools import setup, Extension

neoscrypt_module = Extension('neoscrypt',
                             sources=['neoscrypt/neoscryptmodule.c',
                                      'neoscrypt/neoscrypt.c'],
                             include_dirs=['.', 'neoscrypt'])

setup (name = 'neoscrypt',
       version = '1.2',
       description = 'Bindings for the NeoScrypt proof-of-work algorithm',
       author = 'John Doering',
       author_email = 'ghostlander@phoenixcoin.org',
       url = 'https://github.com/ghostlander/NeoScrypt, ',
       ext_modules = [neoscrypt_module],
       zip_safe = True)
