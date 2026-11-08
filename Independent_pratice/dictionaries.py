# Practicing dictionaries 

# # task1 - creating a dictionary 
# Student = {"Name":"Alex", "Age":"19", "Course":"Computer Science", "University":"leeds"}

# print(Student["Name"])
# print(Student["Age"])
# # print(Student["Course"])


# # task 2 - update dictionary
# Student = {"Name":"Alex", "Age":"19", "Course":"Computer Science", "University":"leeds"}

# Student["Age"] = 20 
# Student["year"] = 1
# print(Student)

# task 3 - printing dictionary contents 
# marks = {
#     "Maths": 85,
#     "Computer Science": 92,
#     "Chemistry": 78,
#     "English": 81
# }

# for mark in marks:
#     print(mark, marks[mark])

# # task 4 - finding highest mark
# marks = {
#     "Maths": 85,
#     "Computer Science": 92,
#     "Chemistry": 78,
#     "English": 81
# }

# highest_mark = marks["Maths"]
# # set first value to highest at default

# for mark in marks:
#     if marks[mark] > highest_mark:
#         highest_mark = marks[mark]

# print(highest_mark)


# # task 5 - counting values 
# # Write a programme that counts how many students achieved a mark of 70 or above.

# scores = {
#     "Alex": 65,
#     "Sarah": 82,
#     "James": 45,
#     "Emily": 91,
#     "Tom": 72
# }
# total = 0
# for score in scores: 
#     if scores[score] >= 70:
#         total +=1 

# print(f"{total} students scored 70 or above")

# task 6 - nested dcitionaries 
students = {
    "Alex": {
        "age": 19,
        "mark": 85
    },
    "Sarah": {
        "age": 20,
        "mark": 92
    },
    "James": {
        "age": 18,
        "mark": 76
    }
}

# # printing sarahs mark
# print(students["Sarah"][ "mark"])

# # changing james's mark 
# students["James"]["mark"] = 80

# # adding a new student
# students["Emily"] = {"age":"18", "mark": "70"}
# print(students)

# Word frequency counter 
# sentence = "hello world hello python world hello"

# individual = sentence.split()

# word_count = {}

# for words in individual: 
#     if words in word_count: 
#         word_count[words] +=1 
#     else: 
#         word_count[words] = 1

# print(word_count)