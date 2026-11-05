# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """
        Checks name is a string and birth is a date object 
        """

        if not isinstance(name, str):
            raise TypeError("name is not a string")

        if name == "":
            raise ValueError("name cant be an empty string")

        if not isinstance(birth, date):
            raise TypeError("birth is not a date object")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initials of the person, in uppercase.
        """

        name_split = self.name.split()
        length = len(name_split)
        initals = ""

        # create a list to store initals
        for names in name_split:
            initals_to_add = names[0]
            initals += initals_to_add


        initals_uppercase = initals.upper()
        
        return initals_uppercase

    def is_birthday(self):
        """
        Tests whether it is the users birthday, return true if so.
        """
        if self.birth == date.today():
            return True 
        else:
            return False


