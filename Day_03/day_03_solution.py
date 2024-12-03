# Solution for Day 02 of Advent of Code 2024
import re

# Part 1
with open("Day_03/input_data.txt", "r") as file:
    corrupted_memory = "".join([line.strip() for line in file])

matching = re.findall(r"mul\([\d]{1,3}\,[\d]{1,3}\)", corrupted_memory)
# matching = regex_pattern.search(corrupted_memory)
muls = [
    list(map(int, mul.replace("mul(", "").replace(")", "").split(",")))
    for mul in matching
]
total = 0
for mul in muls:
    total += mul[0] * mul[1]

# Part 2
new_matching = re.findall(r"don't|do|mul\([\d]{1,3}\,[\d]{1,3}\)", corrupted_memory)
new_total = 0
do_stuff = True
for mul in new_matching:
    if mul == "don't":
        do_stuff = False
    elif mul == "do":
        do_stuff = True
    elif mul.startswith("mul(") and do_stuff:
        _mul = list(map(int, mul.replace("mul(", "").replace(")", "").split(",")))
        new_total += _mul[0] * _mul[1]
    else:
        continue

with open("Day_03/output_data.txt", "w") as file:
    file.write(f"First total: {total}" + "\n")
    file.write(f"Second total: {new_total}")
