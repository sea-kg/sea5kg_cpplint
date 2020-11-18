"""Generic Setup script, takes package info from __pkginfo__.py file."""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sea5kg_cpplint',
    version='v0.0.1',
    install_requires=[],
    keywords=['cpplint'],
    author='Evgenii Sopov',
    author_email='mrseakg@gmail.com',
    description='Python App for cpplint',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sea-kg/sea5kg_cpplint',
    packages=['sea5kg_cpplint'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ),
    python_requires='>=3.6',
)
