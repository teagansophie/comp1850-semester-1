import timeit
from image import Image

# Testing Operatio1: Creating an image 

def create_image():
    Image.create(100,100)

time_taken = timeit.timeit(create_image, number = 100)

print(time_taken)

