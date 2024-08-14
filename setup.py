from setuptools import setup, find_packages

setup(
    name="NetLocator",
    version="1.0.0",
    author="Yasiru Perera",
    author_email="yasiruperera681@gmail.com",
    url="https://github.com/ylp1455/netLocator",
    description="NetLocator is a Python utility designed to quickly retrieve the current IPv4 address of your machine.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=["click"],
    entry_points={"console_scripts": ["get-ip = netLocator:get_ip_address"]},
)
