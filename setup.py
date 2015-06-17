try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple version of grep',
    'author': 'Tyler McGinnis',
    'url': 'http://www.github.com/tylerm-/logfind',
    'author_email': 'tylermcginnis@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)