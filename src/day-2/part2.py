scores = {
    "A": {
        "Y": 1 + 3,
        "Z": 2 + 6,
        "X": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "Z": 1 + 6,
        "X": 2 + 0,
        "Y": 3 + 3,
    },
}

s = 0

with open("input.txt") as f:
    for line in f:
        one, two = line.strip().split()
        s += scores[one][two]
print(s)
