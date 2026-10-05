# list comprehension
# offers a shorter syntax for when you want to create a new list based on
# the values of an existing list 

vegetables = ["leek", "potato","carrot"]
new_list = [x for x in vegetables if "a" in x]
# print(new_list)

# * Given a list `x`, what is the difference between these two lines of code?

#   ```python
#   x.sort()
#   sorted(x)
#   ```

vegetables.sort()
print(vegetables)
print(sorted(vegetables))
# x.sort() sorts the list x in place and returns None, modifying the original list.
# sorted(x) returns a new sorted list without modifying the original list x.

# + `namedtuple`
# + `deque`
# + `Counter`

# namedtuple - assign meaning to each position in a tule and allow for more reable, selfdocumenting code 
