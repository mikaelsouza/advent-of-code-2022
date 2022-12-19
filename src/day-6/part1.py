with open("input.txt") as f:
    text = f.read()

for i in range(0, len(text) - 4):
    if len(set(text[i : i + 4])) == 4:
        print(i + 4)
        break
