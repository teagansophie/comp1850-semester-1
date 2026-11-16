import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
try:
    random_num = int(input("Enter a number"))

except:
    print("Input must be a number.")


# from the list, avoiding any duplicate choices
selected = random.sample(names, k=random_num)

# Display the chosen names, one per line
for name in selected:
        with open("names.txt", "w") as outfile:
             outfile.write(name + "\n")

print(selected)