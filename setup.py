from setuptools import setup, find_packages
from pydot.data_ import setup_info

setup(
    name=setup_info["name"],
    version=setup_info["version"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "pydot= pydot.main:cli",
        ],
    },
)
