import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[0].split(",")

total = 0
for code in myinput:
    current = 0
    for c in code:
        current += ord(c)
        current = (current * 17) % 256
    total += current
print(total)