"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
raw_message1 = raw_message.strip() #removes spaces or newlines from the beginning and end of the string
raw_message2 = raw_message.title() #capitalizes the first character of each word in
raw_message3 = raw_message.replace("a", "@") #replaces all instances of the letter 'a' with '@'
raw_message4 = raw_message.upper() #changes all characters to uppercase

print(f"Original message: {raw_message} \nCleaned message: {raw_message4}")
print(f"Original length: {len(raw_message)} characters")
print(f"Cleaned length: {len(raw_message4)} characters")
# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
