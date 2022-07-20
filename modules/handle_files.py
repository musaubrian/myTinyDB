#!/usr/bin/python3
"""
Module creates a directory in the systems home directory,
"""
import os
from pathlib import Path


home_path = Path.home()
dir_name = ".mydb"
to_dir_path = os.path.join(home_path, dir_name)


def change_to_home():
    """changes directory to the system's home path"""
    os.chdir(home_path)


def create_dir():
    """
    calls change_to_home function
    then creates  directory in the home dir
    """
    change_to_home()
    os.mkdir(dir_name)
