from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst')) as f:
    long_description = f.read()

setup(
    name='projectoxford',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.1.3',

    description='This project extends the Project Oxford API surface to support Python.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/scsouthw/project-oxford-python',
    download_url='https://github.com/scsouthw/project-oxford-python',

    # Author details
    author='Microsoft',
    author_email='scsouthw@microsoft.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # operating systems
        'Operating System :: OS Independent',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2.7', todo: support python 2.7
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='computer vision face detection linguistics language project oxford',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    test_suite='tests.projectoxford_tests'
)
