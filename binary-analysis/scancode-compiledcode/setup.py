#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from glob import glob
from os.path import basename
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

desc = '''A ScanCode scan plugin to get lkmclue, dwarf, gwt, cpp includes, code/comments lines generated code and elf info.'''

setup(
    name='scancode-compiledcode',
    version='2.0.0',
    license='Apache-2.0',
    description=desc,
    long_description=desc,
    author='nexB',
    author_email='info@aboutcode.org',
    url='https://github.com/nexB/scancode-plugins/binary-analysis/scancode-compiledcode',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords=[
        'open source', 'scancode', 'dwarf', 'lkmclue', 'elf', 'cpp includes', 'gwt',
    ],
    install_requires=[
        'scancode-toolkit',
        'attr',
        'pyelftools',
    ],

    extra_requires={
        'binary': [
            'scancode-ctags',
            'scancode-dwarfdump',
            'scancode-readelf',
        ]
    },
    entry_points={
        'scancode_scan': [
            'scancode-lkmclue = lkmclue:LKMClueScanner',
            'scancode-elf = elf:ELFScanner',
            'scancode-cppincludes = cppincludes:CPPIncludesScanner',
            'scancode-dwarf = dwarf:DwarfScanner',
            'scancode-gwt = gwt:GWTScanner',
            'scancode-makedepend = makedepend:MakeDependScanner',
            'scancode-javaclass = javaclass:JavaClassScanner',
            'scancode-codecommentlines = sourcecode:CodeCommentLinesScanner',
        ],
    }
)
