# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):

        if not isinstance(name, str):
            raise TypeError("name is not a string")

        if name == "":
            raise ValueError("name cant be an empyu string")

        if not isinstance(birth, date):
            raise TypeError("birth is not a date object")
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
