import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

total = 0
for n, line in enumerate(myinput):
    line = line[line.index(": ")+2:]
    games = line.split(";")
    valid = True
    counts = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        draws = game.split(",")
        for draw in draws:
            count, name = draw.strip().split(" ")
            count = int(count)
            counts[name] = max(count, counts[name])
    total += counts["red"] * counts["green"] * counts["blue"]
print(total)