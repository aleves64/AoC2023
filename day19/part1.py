import os
import re

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n\n")

tokenizer = re.compile(r"(([xmas][><][0-9]+:[a-zAR]+)|[a-zAR]+)")
subtokenizer = re.compile(r"([xmas])([><])([0-9]+):([a-zAR]+)")
workflows = {}
ends = {}
for workflow in myinput[0].split("\n"):
    tokens = [x[0] for x in tokenizer.findall(workflow)]
    name = tokens[0]
    end = tokens[-1]
    ends[name] = end
    workflows[name] = []
    for token in tokens[1:-1]:
        category, comparison, required_value, dest = subtokenizer.match(token).groups()
        workflows[name].append((category, comparison, int(required_value), dest))

parts = []
subtokenizer = re.compile(r"([xmas])=([0-9]+)")
for rating in myinput[1].split("\n")[:-1]:
    tokens = rating[1:-1].split(",")
    part_dict = {}
    for token in tokens:
        category, score = subtokenizer.match(token).groups()
        part_dict[category] = int(score)
    parts.append(part_dict)

def compare(val1, val2, key):
    if key == "<":
        return val1 < val2
    elif key == ">":
        return val1 > val2

def accepted(part, workflow_key):
    if workflow_key == "A" or workflow_key == "R":
        return workflow_key == "A"

    workflow = workflows[workflow_key]
    for rule in workflow:
        category, comparison, required_value, dest = rule
        score = part[category]
        if compare(score, required_value, comparison):
            return accepted(part, dest)
    return accepted(part, ends[workflow_key])

start = "in"
total = 0
for part in parts:
    if accepted(part, start):
        part_sum = sum(part.values())
        total += part_sum
print(total)
