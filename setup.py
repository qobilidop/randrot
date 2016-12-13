"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import find_packages
from setuptools import setup


setup(
    name='randrot',

    use_scm_version=True,

    description='A sample Python project',
    long_description=open('README.md').read(),

    url='https://github.com/qobilidop/randrot',

    author='Bili Dong',
    author_email='qobilidop@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research'
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='random rotation matrix',

    packages=find_packages(),

    install_requires=['numpy'],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest']
)
