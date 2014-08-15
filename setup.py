from distutils.core import setup

setup(
    name='TwStats',
    version='0.1.0',
    author='Christophe Alexandre',
    author_email='chris.perso@gmail.com',
    packages=['twstats', 'twstats.test'],
    scripts=['bin/twstats.py',],
    url='http://pypi.python.org/pypi/TwStats/',
    license='LICENSE',
    description='Gathering Twitter statistics',
    long_description=open('README.md').read(),
    install_requires=[
        'python-twitter == 1.1',
    ],
)
