import os
import re

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[0].split(",")

def get_hash(code):
    current = 0
    for c in code:
        current += ord(c)
        current = (current * 17) % 256
    return current

def add_to_table(code, boxes):
    code = code.split("=")
    label, length = code
    length = int(length)
    box = get_hash(label)
    labels, lengths = boxes[box]
    if label in labels:
        i = labels.index(label)
        lengths[i] = length
    else:
        labels.append(label)
        lengths.append(length)

def remove_from_table(code, boxes):
    code = code.split("-")
    label, length = code
    box = get_hash(label)
    labels, lengths = boxes[box]
    if label in labels:
        i = labels.index(label)
        labels.pop(i)
        lengths.pop(i)

boxes = {i : ([],[]) for i in range(256)}
for code in myinput:
    if "=" in code:
        add_to_table(code, boxes)
    elif "-" in code:
        remove_from_table(code, boxes)

total = 0
for i in range(256):
    labels, lengths = boxes[i]
    for j in range(len(labels)):
        focus = (i + 1)*(j + 1)*lengths[j]
        total += focus
print(total)
