with open("input.txt") as f:
    text = f.read()

size = 14

for i in range(0, len(text) - size):
    if len(set(text[i : i + size])) == size:
        print(i + size)
        break
