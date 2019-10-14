#!/usr/bin/env python

import os
from setuptools import setup


version = '0.0.1'
local_dir = os.path.dirname(__file__)
if len(local_dir) == 0:
    local_dir = '.'
try:
    with open(os.sep.join([local_dir, 'VERSION']), 'r') as fid:
        version = fid.read().strip()
except:
    pass


setup(
    name='bikes',
    version=version,
    description='ML Labs Bootcamp 2019 Group 5 Repo',
    packages=[
        'bikes',
    ],
)
