from pprint import pprint


def char_to_score(c: str):
    if c.isupper():
        return 27 + ord(c) - ord("A")
    else:
        return 1 + ord(c) - ord("a")


with open("input.txt") as f:
    lines = f.read().splitlines()

groups = zip(lines[::3], lines[1::3], lines[2::3])

score = 0

for g1, g2, g3 in groups:
    l = set.intersection(set(g1), set(g2), set(g3))
    score += char_to_score(l.pop())
print(score)
