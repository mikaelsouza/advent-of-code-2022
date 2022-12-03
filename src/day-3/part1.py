def char_to_score(c: str):
    if c.isupper():
        return 27 + ord(c) - ord("A")
    else:
        return 1 + ord(c) - ord("a")


with open("input.txt") as f:
    final_value = 0
    for line in f:
        half = len(line) // 2
        first_half, second_half = set(line[:half]), set(line[half:])
        char = first_half.intersection(second_half).pop()
        final_value += char_to_score(char)
    print(final_value)
