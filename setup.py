import os
import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]
if py_version < (3, 3):
    raise Exception("aiopyramid requires Python >= 3.3.")


here = os.path.abspath(os.path.dirname(__file__))
NAME = 'jwtauth_test'
with open(os.path.join(here, 'README.rst')) as readme:
    README = readme.read()
with open(os.path.join(here, 'CHANGES.rst')) as changes:
    CHANGES = changes.read()

requires = [
    'aiopyramid[gunicorn]',
    'pyramid_jwtauth',
    'pyramid_chameleon'
]

setup(
    name=NAME,
    version='0.0',
    description='jwtauth_test',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='aiopyramid asyncio web wsgi pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite=NAME,
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = jwtauth_test:main
    """,
)
