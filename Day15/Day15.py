with open("input.txt", "r") as f:
    codes = f.read().split(",")


def hasher(string: str) -> int:
    total: int = 0
    for ch in string:
        total = (ord(ch) + total) * 17 % 256

    return total


res = 0
for code in codes:
    res += hasher(code)

print(res)
