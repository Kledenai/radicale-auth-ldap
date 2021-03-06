#!/usr/bin/env python3

from setuptools import setup

setup(
    name="radicale-auth-ldap",
    version="0.1",
    description="LDAP Authentication Plugin for Radicale 2",
    author="Kledenai Ashver",
    license="GNU GPL v3",
    install_requires=["radicale >= 2.0", "ldap3 >= 2.3, < 2.4"],
    packages=["radicale_auth_ldap"])
