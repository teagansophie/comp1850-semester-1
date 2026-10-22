# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """
    odd_count = 0 
    even_count = 0 

    # Complete your code here
    for i in range(0, len(lstIntegers)):
        if lstIntegers[i] % 2 != 0:  # checking if integer is odd
            odd_count +=1
        else:
            even_count +=1
    list = [odd_count, even_count]

    return list


# Check if correct output is produced
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]
