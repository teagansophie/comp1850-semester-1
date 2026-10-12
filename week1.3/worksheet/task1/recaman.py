# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence

k = 0
sequence = [k]

for i in range(1, L):
    k = sequence[i-1] - i 
    if k>0 and k not in sequence:
        sequence.append(k)
    else:
        k = sequence[i-1] + i
        sequence.append(k)

[print(item) for item in sequence]

# print(f"The Recaman sequence of length {L} is: {sequence}")