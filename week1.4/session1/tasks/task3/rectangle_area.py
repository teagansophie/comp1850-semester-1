
# function implementation
width = int(input("What is the width of the rectangle"))
height = int(input("What is the height of the rectangle"))
def rectangle_area(width,height):  # define suitable input data
    """Returns the area of a rectangle given its width and height"""
    area = width*height             # implement the function
    return area         # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(width,height)}")   # provide suitable data matching your inputs
