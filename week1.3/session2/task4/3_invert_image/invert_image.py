# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"


specified_height = int(input("Enter specified height:"))
original_pixel_value = int(input("Enter pixles:"))
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
        invert_pixel_value = max_gray - original_pixel_value



