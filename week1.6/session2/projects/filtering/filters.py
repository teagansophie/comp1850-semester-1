
from webbrowser import get

from image import Image
import sys 



def blur(img):
    """
    Returns the result of a blur filter on an image.
    """

    image = Image.create(img.width, img.height)

    for row in range(1, image.height -1):
        for col in range(1, image.width -1):
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    total = 0
                    total += image.get(r, c)
                    average = total / 9
                    image.set(row, col, average)
    return image



original_image = Image.read("/workspaces/comp1850-semester-1/week1.6/session2/images/coins.pgm")
blurred = blur(original_image)
blurred.write_pgm("coins_blurred.pgm")