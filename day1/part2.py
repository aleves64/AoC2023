import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

digits_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
digits_char = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for line in myinput:
    first_i = 999
    last_i = 999
    first_val = None
    last_val = None
    for num in digits_num:
        if num in line:
            i = line.index(num)
            k = line[::-1].index(num)
            if i < first_i:
                first_i = i
                first_val = num
            if k < last_i:
                last_i = k
                last_val = num
    for j, num in enumerate(digits_char):
        if num in line:
            i = line.index(num)
            if i < first_i:
                first_i = i
                first_val = str(j + 1)
        if num[::-1] in line[::-1]:
            k = line[::-1].index(num[::-1])
            if k < last_i:
                last_i = k
                last_val = str(j + 1)
    val = int(first_val + last_val)
    total += val
print(total)