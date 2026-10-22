# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
try:
    with open("../images/with_comment.pgm", "r") as infile:
        for line in infile:
            print(line.strip())
except:
    print("file is empty")


# analyse the header, dimensions are on the third line. read each line, turn into int 

