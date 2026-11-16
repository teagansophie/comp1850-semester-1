# See README.md for instructions on what to do this program

import random

random.seed(25)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)


#with seed the same sequence is being generated as we are giving the random algotithm a starting point
#whereas without the seed different sequences are being produced each time 