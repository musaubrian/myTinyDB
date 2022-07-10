#!/usr/bin/python3
"""class TinyDatabase defines a database"""
import time
import os
import subprocess
from tinydb import Query, TinyDB
from modules.create_dir import CreateDir

<<<<<<< HEAD
path_to_file = CreateDir.change_to_home_dir
with open() as f:
=======
with open('./db_location') as f:
>>>>>>> f29c615c99a0508a87afae076383daa585f8d95d
    location = f.read()

data_base = TinyDB(location)


class TinyDatabase():
    def __init__(self):
        """initialize database instance"""
        self.database = data_base
        self.lookup = Query()

    def insert_content(self):
        """
        insert content to the database
        site_name, user_name, password"""
        self.site_name = input("Sitename: ")
        self.user_name = input("Username: ")
        self.password = input("Password: ")

        self.database.insert(
            {
                'Site': self.site_name,
                'User': self.user_name,
                'Password': self.password
            }
        )
        for _ in range(1):
            print()
            print("*"*51)
            print(
                f"Successfully added <{ self.user_name }>"
                f" and <{ self.site_name }> ✔"
                )
            print("*"*51)
            time.sleep(0.5)

    def search_content(self):
        """
        searches for the site_name entered
        """
        print("*"*40)
        print("🔍Searches for Sites and related info")
        print("*"*40)
        self.search_site = input("Enter sitename: ")
        print(self.database.search(self.lookup.Site == self.search_site))

    def delete_content(self):
        """
        deletes the selected user and related information
        *~the related site and password
        """
        print("*"*37)
        print("Deletes user and related info 💀")
        print("*"*37)
        self.delete_user = input("Enter username: ")
        self.database.remove(self.lookup.User == self.delete_user)
        print(f"Deleted <{ self.delete_user }>")

    def show_all_content(self):
        """prints all the contents of the file to stdout"""
        print(self.database.all())

    def primitive_error_handler(self):
        """option to restart process when input is not valid"""
        print("🤷 Unknown input‼\nStart Over?(y/n)")
        self.start_over = input("~# ")
        if self.start_over == "y":
            subprocess.run("cls" if os.name == "nt" else "clear")
            tinydb_intro()
        else:
            print("Exiting program")
            SystemExit()


def add_content():
    """
    add content in single(once)
    or multiple(several users information in order)
    """
    select_input = input("Multpile or Single input(m/s)\n~# ")
    if(select_input == "m"):
        num_of_times = int(input("~# How many:\n"))
        for _ in range(num_of_times):
            TinyDatabase().insert_content()
            print()
    else:
        TinyDatabase().insert_content()
        print()


def tinydb_intro():
    """welcome the user & propmt for input"""
    print("""
**********************************************

                    TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
                (a / s / d / sh)
**********************************************
""")
    options = ["a", "s", "d", "sh"]
    intro_question = input("~# ")
    if intro_question == "a":
        add_content()
    elif intro_question == "s":
        TinyDatabase().search_content()
    elif intro_question == "d":
        TinyDatabase().delete_content()
    elif intro_question == "sh":
        TinyDatabase().show_all_content()
    elif intro_question not in options:
        TinyDatabase().primitive_error_handler()


def launch_db():
    tinydb_intro()
