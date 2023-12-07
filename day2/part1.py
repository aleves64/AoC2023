import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

maxes = {"red": 12, "green": 13, "blue": 14}
total = 0
for n, line in enumerate(myinput):
    line = line[line.index(": ")+2:]
    games = line.split(";")
    valid = True
    for game in games:
        draws = game.split(",")
        for draw in draws:
            count, name = draw.strip().split(" ")
            count = int(count)
            if count > maxes[name]:
                valid = False
        if not valid:
            break
    if valid:
        total += n + 1
print(total)