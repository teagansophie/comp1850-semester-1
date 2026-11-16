import random

random_input = int(input("Random Numbers:"))
f = open("random.txt", "w")

for i in range(random_input):
    with open ("random.txt", "w") as outfile:
        num = random.randint(0,100)
        outfile.write(f"{num}\n")

