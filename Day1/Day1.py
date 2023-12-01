import re

with open('input.txt', 'r') as file:
    data = file.read().splitlines()


def part_one(result: int = 0) -> int:
    for line in data:
        new_line: str = re.sub(r'[A-z]', '', line)
        number_found: str = new_line[0] + new_line[-1]
        result += int(number_found)
    return result


digit_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

