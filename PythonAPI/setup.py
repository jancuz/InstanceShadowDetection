from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pysobatools._mask',
        sources=['./common/maskApi.c', 'pysobatools/_mask.pyx'],
        include_dirs = [np.get_include(), './common'],
        #extra_compile_args=['gcc': ['/Qstd=c99']],
    )
]

setup(
    name='pysobatools',
    packages=['pysobatools'],
    package_dir = {'pysobatools': 'pysobatools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='2.0',
    ext_modules= ext_modules
)
