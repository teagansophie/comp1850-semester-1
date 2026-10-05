# Worksheet 1.2: Task 1 Solution

try:
    grade = int(input("Enter a grade in the range 0-100: "))

    if grade<0 or grade>100:
        print("Error: Grade must be an integer between 0 and 100")
        import sys
        sys.exit("Error!")
    else:
        if grade>=70:
            print(grade,"is a Distinction")
        elif grade>=40 and grade<70:
            print(grade,"is a Pass")
        else:
            print(grade,"is a Fail")
except:
    print("Error: Grade must be an integer between 0 and 100")
    import sys
    sys.exit("Error!")