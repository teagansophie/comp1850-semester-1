# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator = "-"):
    # complete your code here
    # day = "m"
    # month = "jan"
    # year = "2008"

    formatted_date = f"{day:02d}{separator}{month}{separator}{year}"
    return formatted_date

print(format_data("01", "01", "2008"))
# Write code to test the function with separators such as "/", ":", "."
