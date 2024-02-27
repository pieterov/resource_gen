"""
Purpose:        Define constants used at general level
Description:    These are independent of functions and constants.
Author:         Pieter Overdevest
"""

# Import package.
import os
import re

# Path to partner folder
C_PATH_ROOT_PARTNER = re.search(r'.+/Partners/', os.getcwd()).group()

# Path to project folder.
C_PATH_ROOT_PROJECT = re.sub("Code", "", os.getcwd())

# Paths to project root folder and sub-folders.
C_PATH_CODE         = os.path.join(C_PATH_ROOT_PROJECT, "Code")
C_PATH_DATA         = os.path.join(C_PATH_ROOT_PROJECT, "Data")
C_PATH_DELIVERABLES = os.path.join(C_PATH_ROOT_PROJECT, "Deliverables")
C_PATH_DOCUMENTS    = os.path.join(C_PATH_ROOT_PROJECT, "Documents")
C_PATH_IMAGES       = os.path.join(C_PATH_ROOT_PROJECT, "Images")