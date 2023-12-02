# part 1 : 12 red cubes, 13 green cubes,  14 blue cubes

with open('input.txt', 'r') as file:
    games = file.read().splitlines()

# line_id = list(range(1, 100))
# for index_line, line in enumerate(games):
#     games = line.split(": ")[1]
#     id_game = index_line + 1
#     rounds = games.split("; ")
#     for i in range(id_game):
#         for j in range(len(rounds)):
#             colors = rounds[j].split(", ")
#             for x in range(len(colors)):
#
#                 value, key = colors[x].split(" ")
#                 if (key == "red" and int(value) > 12) \
#                         or (key == "green" and int(value) > 13) \
#                         or (key == "blue" and int(value) > 14):
#                     try:
#                         line_id.remove(id_game)
#                     except ValueError:
#                         continue
# print(sum(line_id))

# part 2 : sum of power of fewest

result = 0


arr = []
for index_line, line in enumerate(games):
    games = line.split(": ")[1]
    id_game = index_line + 1
    rounds = games.split("; ")
    games = games.replace(";", ",").split(", ")
    arr_green = []
    arr_blue = []
    arr_red = []

    for i in games:
        if "green" in i:
            arr_green.append(int(i.split(" ")[0]))

        if "red" in i:
            arr_red.append(int(i.split(" ")[0]))

        if "blue" in i:
            arr_blue.append(int(i.split(" ")[0]))

    max_green = max(arr_green)
    max_blue = max(arr_blue)
    max_red = max(arr_red)

    result += max_green*max_blue*max_red


print(result)