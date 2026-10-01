"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Teagan Liddle
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    month_saving = int(input("How much money would you like to save every month? "))
    # Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    total_savings = month_saving * 12
    # print this out for the user with a suitable message.
    print(f"You will have saved £{total_savings} by the end of the year.")
    # Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    interest = total_savings * 0.008
    total_with_interest = total_savings + interest #calculate the total amount including interest

    # print this out in the format £X.XX (to two decimal places).
    print(f"You will have saved £{total_with_interest:.2f} by the end of the year including interest.")
except: # Validate that they have entered an integer.
    print("Please enter a valid integer.")
    

