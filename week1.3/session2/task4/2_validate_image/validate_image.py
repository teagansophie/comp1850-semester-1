# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

specified_height = int(input("Enter specified height:"))
specified_pixles = int(input("Enter pixles:"))
specified_width = int(input("Enter width:"))

with open("images/feep.pgm", "r") as infile:
    valid_lines = [] # list of valid information excluding comments and whitespaces

    for lines in infile:
        line = line.strip() # splits lines up

        if line!= " " and not line.startswith("#"):
            valid_lines.append(line)
        
        #need to split up width and height as they are stores together 
        dimensions = valid_lines[1].split()
        width = int(dimensions[0])
        height = int(dimensions[1])
        pixel_rows = valid_lines[3:]

        image_dimensions = width*height 

        #max gray value is read from 3rd line without comments
        max_gray = int(valid_lines[2])

        if len(pixel_rows) != specified_pixles: 
            print("invalid height")
        elif width != specified_width:
            print("Invalid witdh")

        elif height != specified_height:
            print("Inavlid height")
        else:
            print("Valid image")

