
with open('input.txt', 'r') as file:
    lottery = file.read().splitlines()

result = 0
found = 0
tracking_map = {}

for index, line in enumerate(lottery):
    if index not in tracking_map:
        tracking_map[index] = 1

    D = line.split(":")[1]
    numbers_picked, numbers_to_check = [list(map(int, i.split())) for i in D.split("|")]

    # True + True = 2
    found = sum(number in numbers_picked for number in numbers_to_check)

    for next_card in range(index + 1, index + found + 1):  # card 1 in range(1, 5)
        tracking_map[next_card] = tracking_map.get(next_card, 1) + tracking_map[index]  # adding the times we got the card


print(sum(tracking_map.values()))



# What learnt today:
# 1. we can use map to wash string to int
# 2. note True + True = 2, we can use to find a number existing in both side
# 3. need to use more list comprehension
# 4. why tracking_map[index] is the times we got the card?



