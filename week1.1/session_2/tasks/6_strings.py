# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"Modified String 1: {user_string.lower()}") #changes first character to lowercase
print(f"Modified String 2: {user_string.upper()}") #changes all characters to uppercase
print(f"Modified String 3: {user_string.strip()}") #removes spaces or newlines from the beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces all instances of the letter 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}") #capitalizes the first character of the string
print(f"Modified String 6: {user_string[::-1]}") #reverses the string 
print(f"Modified String 7: {user_string.title()}") #capitalizes the first character of each word in the string
print(f"Modified String 8: {len(user_string)}") #returns the length of the string 
print(f"Modified String 9: {user_string.find('a')}") #returns the index of the first occurrence of the letter 'a'
print(f"Modified String 10: {user_string.count('a')}") #returns the number of occurrences of the letter 'a' in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")#returns how many times 'a' appears in the string
print(f"Modified String 12: {user_string.endswith('!')}") #returns True if the string ends with '!', otherwise returns False
print(f"Modified String 13: {user_string.isalnum()}") #returns True if the string is alphanumeric (contains only letters and numbers), otherwise returns False
print(f"Modified String 14: {user_string.isalpha()}") #returns True if the string is alphabetic (contains only letters), otherwise returns False
print(f"Modified String 15: {user_string.isdigit()}") #returns True if the string is numeric (contains only digits), otherwise returns False



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!