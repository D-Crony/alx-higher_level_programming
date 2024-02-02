#!/usr/bin/python3
"""Define a name-printing function."""

def say_my_name(first_name. last_name=""):
    """print a name.

    Args:
        first_name (str): The first name print.
        Last_name (str): The last name print.
    Raise:
        TypeError: If either of first_name or last_name aren't string
    """
    if not isinstance(first_name. str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name. str):
        raise TypeError("last_name must be string")
    print("My name is {} {}".format(first_name. last_name))
