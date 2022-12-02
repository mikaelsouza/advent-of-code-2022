elves = [0]

with open("src/day-1/input.txt") as f:
    for line in f:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1] += int(line)
    top_3 = sum(sorted(elves, reverse=True)[0:3])
    print(f"Top 3 elves calories: {top_3}")
    