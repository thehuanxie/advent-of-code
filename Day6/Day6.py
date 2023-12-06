import re

with open("input.txt", "r") as file:
    ts = file.read().strip().splitlines()

arr = []
for line in ts:
    arr.append(re.findall(r'\d+', line))

t = arr[0]
d = arr[1]

time = str()
distance = str()
for i in t:
    time += i

for i in d:
    distance += i

time, distance = (int(time), int(distance))

count = 0
for v in range(time + 1):
    if (time - v) * v > distance:
        count += 1
print(count)


#############################################
#                 part 1                    #
#############################################

# t = map(int, arr[0])
# s = map(int, arr[1])
#
# arr = list(zip(t, s))
#
#
# res = []
# for time, distance in arr:
#     count = 0
#     for v in range(time+1):
#
#         if (time - v) * v > distance:
#             count += 1
#     res.append(count)
# print(res)
# multi = 1
# for nb in res:
#     multi *= nb
#
# print(multi)