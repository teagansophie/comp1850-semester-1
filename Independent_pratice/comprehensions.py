# a comprehension is a shorter way of creating a new data structure using a loop 
# expression for item in iterable if condition

# numbers = [2, 4, 6, 8, 10]
# doubled_numbers = [number * 2 for number in numbers]
# print(doubled_numbers)

# # task2 - only nums larger than 10
# numbers = [1, 5, 8, 12, 15, 20, 23]
# larger_than_ten = [number for number in numbers if number>10]
# print(larger_than_ten)

# # task 3 - uppercase w strings 
# names = ["alice", "BOB", "charlie", "DAVID"]
# uppercase_names = [name.upper() for name in names]
# print(uppercase_names)

# # filtering strings 
# animals = ["dog", "cat", "elephant", "cow", "giraffe"]
# long_names = [animal for animal in animals if len(animal) > 3]
# print(long_names)

# # if/else expressions 
# numbers = [1, 2, 3, 4, 5, 6]
# odd_or_even = ["even" if number % 2 == 0 else "odd" for number in numbers]

# # set comprehension 
# numbers = [2, 4, 2, 6, 4, 8, 8, 10]
# unique_numbers = {number for number in numbers}
# print(unique_numbers)

# set comprehension w strings
subjects = ["Maths", "MATHS", "Computer Science", "computer science", "Physics"]
clean_subjects = {subject.lower() for subject in subjects }
print(clean_subjects)