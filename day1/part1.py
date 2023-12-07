import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

total = 0
for line in myinput:
    numbers = [c for c in line if c.isdigit()]
    total += int(numbers[0] + numbers[-1])
print(total)