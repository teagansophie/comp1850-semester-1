# Worksheet 1.2: Task 2 Solution

# try:
#     user_input = input("e")
try:
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    print(numbers)

    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / len(numbers)

    except:
        print("Error: no numbers provided")
        sys.exit()

if len(numbers) % 2 != 0:
   sorted_numbers = sorted(numbers)
   
else:
    print("The list has an even number so no median can be calculated.")
