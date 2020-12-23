import os
import sys
import setuptools

sys.path.insert(0, os.path.abspath('./source'))

import round_utils

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
    description=round_utils.__doc__
)
