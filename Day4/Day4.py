from collections import defaultdict
import math

with open('input.txt', 'r') as file:
    lottery = file.read().splitlines()

result = 0
found = 0
for index, line in enumerate(lottery):
    D = line.split(":")[1]
    numbers_picked, numbers_to_check = [list(map(int, i.split())) for i in D.split("|")]

    # True + True = 2
    found = sum(number in numbers_picked for number in numbers_to_check)

    if found > 0:
        result += 2 ** (found-1)

print(result)





