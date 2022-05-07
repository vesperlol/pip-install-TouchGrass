from setuptools import setup, find_packages


__name__ = "TouchGrass"
__version__ = "69"
setup(
    name=__name__,
    version=__version__,
    license='MIT',
    author="vesper",
    author_email='email@example.com',
    packages=find_packages(),
    url='https://github.com/vesperlol/pip-install-TouchGrass',
    keywords='outside, grass, lib, module',
    install_requires=[
          'requests',
      ],

)