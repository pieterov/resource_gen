"""
Purpose:        Define variables used at general level
Description:    These depend on functions and constants.
Author:         Pieter Overdevest
"""

# Import package.
import os
import re

# Path to project folder.
C_PATH_PROJECT_ROOT = re.sub("Code", "", os.getcwd())

# Paths to project root folder and sub-folders.
C_PATH_CODE         = os.path.join(C_PATH_PROJECT_ROOT, "Code")
C_PATH_DATA         = os.path.join(C_PATH_PROJECT_ROOT, "Data")
C_PATH_DELIVERABLES = os.path.join(C_PATH_PROJECT_ROOT, "Deliverables")
C_PATH_DOCUMENTS    = os.path.join(C_PATH_PROJECT_ROOT, "Documents")
C_PATH_IMAGES       = os.path.join(C_PATH_PROJECT_ROOT, "Images")