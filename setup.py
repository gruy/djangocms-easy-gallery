#!/usr/bin/env python

from setuptools import setup


version = '0.1'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name='djangocms-easy-gallery',
    version=version,
    url='https://bitbucket.org/gruy/djangocms-easy-gallery',
    author='Cyrill Popov',
    author_email='gruy@feodosia.net',
    license='LICENSE',
    packages=['djangocms_easy_gallery', 'djangocms_easy_gallery.migrations', ],
    description=('Django CMS plugin for create easy image gallery (include Lightbox2).'),
    keywords=['editor', 'django-cms', 'django', ],
    classifiers=classifiers,
    long_description=open('README').read(),
    install_requires=['django-cms>=3', ],
    include_package_data=True,
    zip_safe=False
)
