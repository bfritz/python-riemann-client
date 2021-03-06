#!/usr/bin/env python2.6

import setuptools

setuptools.setup(
    name='riemann-client',
    version='4.0.1',

    author="Sam Clements",
    author_email="sam.clements@datasift.com",

    url="https://github.com/borntyping/python-riemann-client",
    description="A Riemann client and command line tool",
    long_description=open('README.rst').read(),
    license="MIT",

    packages=setuptools.find_packages(),

    install_requires=[
        'argparse>=1.1',
        'protobuf>=2.3.0',
    ],

    entry_points={
        'console_scripts': [
            'riemann-client = riemann_client.command:main',
        ]
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration'
    ],
)
