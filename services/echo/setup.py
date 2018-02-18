#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name = "echo",
    packages = ['src/echo'],
    description = "echo service",
    entry_points={
        'console_scripts': [
            'service=echo.main.run',
        ],
    },
)
