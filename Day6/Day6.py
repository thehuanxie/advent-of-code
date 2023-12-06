import re

with open("input.txt", "r") as file:
    ts = file.read().strip().splitlines()

arr = []
for line in ts:
    arr.append(re.findall(r'\d+', line))

t = map(int, arr[0])
s = map(int, arr[1])

arr = list(zip(t, s))


res = []
for time, distance in arr:
    count = 0
    for v in range(time+1):

        if (time - v) * v > distance:
            count += 1
    res.append(count)

multi = 1
for nb in res:
    multi *= nb

print(multi)