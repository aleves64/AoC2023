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

def interval_intersections(intervals1, intervals2):
    new_intervals = []
    n = len(intervals1)
    m = len(intervals2)
    i = j = 0
    while i < n and j < m:
        x0, x1 = intervals1[i]
        y0, y1 = intervals2[j]
        new_interval = (max(x0, y0), min(x1, y1))
        if x1 < y1:
            i += 1
        else:
            j += 1
        new_intervals.append(new_interval)
    return new_intervals

def rule_intersection(rule1, rule2):
    new_intervals = {}
    for c in "xmas":
        new_intervals[c] = interval_intersections(rule1[c], rule2[c])
    return new_intervals

def chop_interval(category, comparison, required_value):
    new_intervals = {c: [(1,4000)] for c in "xmas"}
    if comparison == "<":
        new_intervals[category] = [(1, required_value - 1)]
    elif comparison == ">":
        new_intervals[category] = [(required_value + 1, 4000)]
    return new_intervals

def reverse_chop(category, comparison, required_value):
    new_intervals = {c: [(1,4000)] for c in "xmas"}
    if comparison == "<":
        new_intervals[category] = [(required_value, 4000)]
    elif comparison == ">":
        new_intervals[category] = [(1, required_value)]
    return new_intervals

def size_intervals(remaining):
    total = 1
    for category in remaining:
        category_sum = 0
        for start, end in remaining[category]:
            category_sum += end - start + 1
        total *= category_sum
    return total

def accepted_intervals(workflow_key, remaining):
    if workflow_key == "A":
        return size_intervals(remaining)
    elif workflow_key == "R":
        return 0

    workflow = workflows[workflow_key]
    res_intervals = []

    for rule in workflow:
        category, comparison, required_value, dest = rule
        chopped_interval = chop_interval(category, comparison, required_value)
        remaining_dest = rule_intersection(remaining, chopped_interval)
        dest_accepts = accepted_intervals(dest, remaining_dest)
        res_intervals.append(dest_accepts)

        reverse_chopped = reverse_chop(category, comparison, required_value)
        remaining = rule_intersection(remaining, reverse_chopped)

    end_accepts = accepted_intervals(ends[workflow_key], remaining)
    res_intervals.append(end_accepts)
    return sum(res_intervals)

workflow_key = "in"
remaining = {c: [(1,4000)] for c in "xmas"}
total = accepted_intervals("in", remaining)
print(total)
