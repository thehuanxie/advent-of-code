import re

with open('input.txt', 'r') as file:
    data = file.read().splitlines()


def part_one(data:list, result: int = 0) -> int:
    pattern = r'[A-z]'
    pattern_compiled = re.compile(pattern)
    for line in data:
        new_line: str = pattern_compiled.sub('', line)
        number_found: str = new_line[0] + new_line[-1]
        result += int(number_found)
    return result


print('part 1:', part_one(data))


digit_dict = {"one": "o1e",
              "two": "t2o",
              "three": "t3e",
              "four": "f4r",
              "five": "f5e",
              "six": "s6x",
              "seven": "s7n",
              "eight": "e8t",
              "nine": "n9e"}

f = open("input.txt", "r")
text = f.read()

for key, value in digit_dict.items():
    text = text.replace(key, value)

text_in_line = text.splitlines()

print('part 2:', part_one(text_in_line))