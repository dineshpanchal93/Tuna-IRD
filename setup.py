from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tuna_ird/__init__.py
from tuna_ird import __version__ as version

setup(
	name="tuna_ird",
	version=version,
	description="Reports & Sales Invoice Changes",
	author="dineshpanchal432@gmail.com",
	author_email="dineshpanchal432@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
