with open("input.txt", "r") as f:
    camelC = f.read().splitlines()

record = {}
game_order = {
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "T": "V",
    "J": "W",
    "Q": "X",
    "K": "Y",
    "A": "Z"
}

for line in camelC:
    key, value = line.split()
    for k, v in game_order.items():
        key = key.replace(k, v)
    record[key] = int(value)

print(record)

res = 0
order = {
    "high_card": dict(),
    "one_pair": dict(),
    "two_pair": dict(),
    "three_of_a_kind": dict(),
    "full_house": dict(),
    "four_of_a_kind": dict(),
    "five_of_a_kind": dict(),

}
for card, value in list(record.items()):
    for c in card:
        count_dict = {i: card.count(i) for i in card}
    print(list(count_dict.values()))

    if list(count_dict.values()).count(1) == 5:
        order["high_card"].update({card: value})
    elif list(count_dict.values()).count(2) == 1 and list(count_dict.values()).count(1) == 3:
        order["one_pair"].update({card: value})
    elif list(count_dict.values()).count(2) == 2:
        order["two_pair"].update({card: value})
    elif list(count_dict.values()).count(3) == 1 and list(count_dict.values()).count(1) == 2:
        order["three_of_a_kind"].update({card: value})
    elif list(count_dict.values()).count(3) == 1 and list(count_dict.values()).count(2) == 1:
        order["full_house"].update({card: value})
    elif list(count_dict.values()).count(4) == 1:
        order["four_of_a_kind"].update({card: value})
    elif list(count_dict.values()).count(5) == 1:
        order["five_of_a_kind"].update({card: value})

res = []
for key, value in order.items():
    sorted_value = dict(sorted(value.items()))
    order[key] = sorted_value
print(order)

for value in order.values():
    for v in value.values():
        res.append(v)
print(res)

t = 0
for i, v in enumerate(res):
    t += (i+1)*v

print(t)
