# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
user_name = input("Whats your name?")
user_age = input("How old are you?")
user_colour = input("Whats your favourite colour?")
# Open a file called 'user_info.txt' for reading
with open("user_infp.txt", "w") as outfile:
    outfile.wrote(f"Name: {user_name}" + "\n")
    outfile.wrote(f"Age: {user_age}" + "\n")
    outfile.wrote(f"Favourite colour: {user_colour}" + "\n")
# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
