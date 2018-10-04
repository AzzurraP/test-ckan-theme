from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-example_theme',
    version=version,
    description="tema custom",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='wbrd',
    author_email='azzurra.pantella@gmail.com',
    url='http://www.dati.umbria.it',
    license='ccby',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.example_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	example_theme=ckanext.example_theme.plugin:ExampleThemePlugin
	""",
)
