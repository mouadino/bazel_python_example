#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name = "api",
    packages = ['src/api'],
    description = "API service",
    entry_points={
        'console_scripts': [
            'service=api.main.run',
        ],
    },
)
