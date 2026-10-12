# Worksheet 1.2: Task 2 Solution

# try:
#     user_input = input("e")
import sys 

try:
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    print(numbers)

    minimum = min(numbers)
    print(f"Minimum = {minimum}")
    maximum = max(numbers)
    print(f"Maximum = {maximum}")
    mean = sum(numbers) / len(numbers)
    print(f"Mean = {mean}")

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 != 0:  # odd length
        median = sorted_numbers[length // 2]
        print(f"Median = {median}")
    else:  # even length
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
        print(f"Median = {median}")

except:
    sys.exit("Error: no numbers provided")

