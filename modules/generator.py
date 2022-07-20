#!/usr/bin/python3
"""module generates random passwords"""
import random


class PasswordGenerator():
    """
    defines PasswordGenerator
    """
    def __init__(self) -> None:
        """initialize the generator"""
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lower = self.upper.lower()
        self.digits = "0123456789"
        self.symbols = "*&%$#@!+~:-<|?/ >"
        self.empty_string = "" + self.upper

    def take_input(self):
        """take user input"""
        self.password_length = int(input("Length of password(int): "))
        self.password_amount = int(input("Number of passwords(int): "))
        if self.password_amount <= 0 or self.password_length <= 0:
            raise ValueError("Input must be > 0")
        self.use_symbols = input("Would you like to use symbols?\n~# ")
        self.use_lower = input("Would you like to use lowercase letters?\n~# ")
        self.use_digits = input("Would you like to use numbers?\n~# ")
        print()

    def start_join(self):
        """generates random vlues and joins them"""
        print("""
****************************************

           Password generator

                yes: y
                no: n

****************************************
    """)
        PasswordGenerator.take_input(self)
        if self.use_symbols == "y":
            self.empty_string += self.symbols
        else:
            pass
        if self.use_digits == "y":
            self.empty_string += self.digits
        else:
            pass
        if self.use_lower == "y":
            self.empty_string += self.lower
        else:
            self.empty_string

        print("\n", "*"*len(self.upper), "\n")
        for _ in range(self.password_amount):
            self.generated_password = "".join(random.sample(
                self.empty_string, self.password_length
                ))
            print(f"~# {self.generated_password}")


start_generator = PasswordGenerator()
