with open("input.txt", "r") as f:
    dataset = f.read().splitlines()

def part_1(arr):
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i+1] - arr[i])
    if all(j==0 for j in new_arr):
        return arr[-1]
    else:
        return arr[-1]+part_1(new_arr)

def part_2(arr):
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i+1] - arr[i])
    if all(j==0 for j in new_arr):
        return arr[0]
    else:
        return arr[0]-part_2(new_arr)

res = 0
for line in dataset:
    input_data = [int(x) for x in line.split()]

    res += part_2(input_data)

print("res", res)



