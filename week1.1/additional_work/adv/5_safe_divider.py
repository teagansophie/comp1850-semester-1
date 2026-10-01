"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""
try:
    numerator_input = int(input("Enter the numerator: "))
    denominator_input = int(input("Enter the denominator: "))
   
    if denominator_input == 0 or numerator_input == 0:
        print("Warning: Division by zero is not allowed.")
    elif denominator_input < 0 or numerator_input < 0:
        print("Warning: Negative numbers are not allowed.")
    else:
        result = numerator_input / denominator_input
        print(f"The result is: {result}")

except:
    print("Please enter valid numbers for numerator and denominator.")
