#!/usr/bin/env python3
"""calls the required modules"""
from pathlib import Path
from my_tinydb.generator import generate_password
from my_tinydb.database import launch_db, full_path
from my_tinydb.handle_files import (
        create_dir, decrypt_file, encrypt_file, to_key
        )
import os
import subprocess
import time


def clear_console():
    """clear the terminal"""
    subprocess.run("cls" if os.name == "nt" else "clear")


def handle_error():
    """clear console and prompts user again"""

    print("\n🤷 Unknown input‼\nStart Over?(y/n)")
    restart = input("~# ")
    if restart == "y":
        encrypt_file(db_path=full_path, key_path=to_key)
        clear_console()
        select_module()
    else:
        print("\nSee you next time🙋")
        time.sleep(1)
        clear_console()
        encrypt_file(db_path=full_path, key_path=to_key)
        SystemExit()


def select_module():
    """Prompt user to select the module they want to use"""
    decrypt_file(db_path=full_path, key_path=to_key)
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
        if Path(full_path).is_file():
            launch_db()
        else:
            create_dir()
    elif user_prompt == "gen":
        clear_console()
        generate_password()
        encrypt_file(db_path=full_path, key_path=to_key)
    elif user_prompt not in choices:
        handle_error()


if __name__ == '__main__':
    """
    run the select_module function
    if KeyboardInterrupt(ctrl+c) is caught;
    else just encrypt the database
    """
    try:
        select_module()
    except KeyboardInterrupt:
        print("\nSee ya next time\n")
        encrypt_file(full_path, to_key)
    finally:
        encrypt_file(full_path, to_key)
