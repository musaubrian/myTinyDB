#!/usr/bin/env python3

from modules.generator import start_generator
from modules.database import launch_db
import os
import time

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def handle_error():
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
    print("""
****************************************
     
        What shall it be today?

            database: db
        password generator: gen

****************************************        
    """)

    choices = ["db", "gen"]
    user_prompt = input("\n~# ")
    if user_prompt == "db":
        clear_console()
        launch_db()
    elif user_prompt == "gen":
        clear_console()
        start_generator.start_join()
    elif user_prompt not in choices:
        handle_error()

if __name__ == '__main__':
    select_module()
