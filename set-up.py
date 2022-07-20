#!/usr/bin/python3
"""
script creates the directories required
and installs required packages
"""
import os
import subprocess
from pathlib import Path
from modules.handle_files import create_dir
from modules.database import full_path
package_name = "tinydb==4.5.2"


def prepare_env(package):
    """
    sets up everything for the user
    """
    if Path(full_path).is_file():
        raise FileExistsError("Directory already exists")
    else:
        create_dir()

    subprocess.run(
            ["pip", "install", package]
            if os.name == "nt"
            else ["pip3", "install", package]
            )
    print("="*17)
    print("Everything is set")


if __name__ == "__main__":

    prepare_env(package_name)
