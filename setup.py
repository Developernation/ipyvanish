from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='ipyvanish',
    version=__version__,
    description='A simple python CLI for the IPVanish VPN',
    long_description=long_description,
    url='https://github.com/limx0/ipyvanish',
    download_url='https://github.com/limx0/ipyvanish/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    author='Bradley McElroy',
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={
        'console_scripts': [
            'ipyvanish = ipyvanish:main'
        ]
    },
    author_email='bradley.mcelroy@live.com'
)
