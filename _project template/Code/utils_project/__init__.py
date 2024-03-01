"""
Purpose:    Init file - Resource Project
Author:     Pieter Overdevest
"""

# Import packages.
import os
import re
import sys

# Path to code folder of this project.
C_PATH_PROJECT_ROOT = re.sub("Code", "", os.getcwd())

# Add path to packages folder.
sys.path.append(
    
    os.path.join(
        re.search(r'.+/Partners/', C_PATH_PROJECT_ROOT).group(),
        'IWD/Packages/'
    )
)

# Import modules.
from .i_constants                   import *

