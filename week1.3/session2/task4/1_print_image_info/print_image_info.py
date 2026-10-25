# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
try:
    with open("images/with_comment.pgm", "r") as infile:
        valid_lines = [] #empty list to store non-comments
        for line in infile: 
            line = line.strip
            #print(line.strip())
            
            if line!= " " and not line.startswith("#"):
                valid_lines.append(line) #stores all lines that is not empty and doesnt start with #

            #need to split up width and height as they are stores together 
            dimensions = valid_lines[1].split()
            width = int(dimensions[0])
            height = int(dimensions[1])

            image_dimensions = width*height 
            print(f"Image Dimensions:{image_dimensions}")

            #max gray value is 15(read from 3rd line without comments)
            max_gray = int(valid_lines[2])
            print(f"Max gray value:{max_gray}")
except:
    print("file is empty")


# analyse the header, dimensions are on the third line. read each line, turn into int 

