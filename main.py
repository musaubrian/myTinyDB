#!/usr/bin/env python3
"""calls the required modules"""
from pathlib import Path
from modules.generator import start_generator
from modules.database import launch_db, full_path
from modules.handle_files import create_dir, delete_setup
import os
import subprocess
import time


def clear_console():
    """clears the terminal"""
    subprocess.run("cls" if os.name == "nt" else "clear")


def handle_error():
    """clears console and prompts user again"""
    print("\n🤷 Unknown input‼\nStart Over?(y/n)")
    restart = input("~# ")
    if restart == "y":
        clear_console()
        select_module()
    else:
        print("\nSee you next time🙋")
        time.sleep(1)
        clear_console()
        SystemExit()


def select_module():
    """Prompts user to select the module they want to use"""
    print("""
****************************************

        what shall it be today?
            database: db
        password generator: gen

****************************************
""")

    choices = ["db", "gen"]
    user_prompt = input("\n~# ")
    if user_prompt == "db":
        clear_console()
        delete_setup()
        if Path(full_path).is_file():
            launch_db()
        else:
            create_dir()
    elif user_prompt == "gen":
        clear_console()
        start_generator.start_join()
    elif user_prompt not in choices:
        handle_error()


if __name__ == '__main__':

    select_module()
