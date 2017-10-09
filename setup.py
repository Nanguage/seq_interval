import os
from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# load about information
about = {}
with open(os.path.join(here, 'seq_interval', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

requires = []

setup(
    name=about['__title__'],
    version=about['__version__'],
    keywords=about['__keywords__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=['seq_interval'],
    package_data={'':['LICENSE'], 'seq_interval': []},
    package_dir={'seq_interval': 'seq_interval'},
    install_requires=requires,
    license=about['__license__'],
    classifiers=(
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    )   
)

