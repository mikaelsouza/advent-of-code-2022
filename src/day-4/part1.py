import re

with open("input.txt") as f:
    lines = f.read().splitlines()

pattern = re.compile(r"\d+")

count = 0

for line in lines:
    numbers = list(int(num) for num in pattern.findall(line))
    r1, r2 = numbers[:2], numbers[2:]
    if (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1]):
        count += 1
    else:
        pass
print(count)
