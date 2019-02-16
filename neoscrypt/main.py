#!/usr/bin/env python
import platform
from ctypes import CDLL, c_char_p

import pkg_resources

sysname = platform.system()

if sysname == 'Darwin':
    lib_name = "neoscrypt.dylib"
elif sysname == 'Windows':
    #python 3.6 x86-mingw32
    lib_name = "neoscrypt.dll"
else:
    lib_name = "neoscrypt.so"
lib_path = pkg_resources.resource_filename('neoscrypt', 'lib/{}'.format(lib_name))
foo = CDLL(lib_path)

bar = foo.bar
bar.restype = c_char_p
bar.argtypes = [c_char_p]

print(bar('hello'))