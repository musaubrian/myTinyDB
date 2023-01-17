#!/usr/bin/python3
"""
script creates the directories required,
installs required packages
"""

import subprocess
from my_tinydb.handle_files import create_dir
import my_tinydb.handle_files


def prepare_env():
    """
    sets up everything for the user
    """
    create_dir()
    my_tinydb.handle_files.generate_key()
    subprocess.check_call(["pip3", "install", "-r", "requirements.txt"])


if __name__ == "__main__":

    prepare_env()
