try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name = 'hanoi_gym',
      version = '0.0.1',
      packages = find_packages()
      author = 'Michael Oyefusi',
      url = "https://github.com/oyefmi/hanoi-gym",
      install_requires = ['numpy', 'gym']
)
