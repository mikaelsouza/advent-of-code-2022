# A, X, 1 -> Rock
# B, Y, 2 -> Paper
# C, Z, 3 -> Scissors

# 0 loss
# 3 draw
# 6 won

scores = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3,
    },
}


s = 0

with open("input.txt") as f:
    for line in f:
        one, two = line.strip().split()
        s += scores[one][two]
print(s)
