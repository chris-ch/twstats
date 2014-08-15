from setuptools import setup

setup(
    name='TwStats',
    version='0.1.0',
    author='Christophe Alexandre',
    author_email='chris.perso@gmail.com',
    packages=['twstats', 'twstats.test'],
    scripts=['scripts/twstats.py',],
    url='http://pypi.python.org/pypi/TwStats/',
    license='LICENSE',
    description='Gathering Twitter statistics',
    long_description=open('README.txt').read(),
    install_requires=[
        'twython>=3.1.2',
    ],
)
