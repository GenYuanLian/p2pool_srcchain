from distutils.core import setup, Extension

Lyra2Z_scrypt_module = Extension('Lyra2Z_scrypt',
                               sources = ['scryptmodule.c',
                                          'blake.c',
                                          'Lyra2.c',
                                          'Lyra2Z.c',
                                          'Sponge.c',
                                          ],
                               include_dirs=['.'])

setup (name = 'Lyra2Z_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by RBTC',
       ext_modules = [Lyra2Z_scrypt_module])
