biggest_val = 0
biggest_elf = 0

cur_val = 0
cur_elf = 0

with open("src/day-1/input.txt") as f:
    for line in f:
        if line == "\n":
            if cur_val > biggest_val:
                biggest_val = cur_val
                biggest_elf = cur_elf
            cur_val = 0
            cur_elf += 1
        else:
            cur_val += int(line)
    print(f"Elf: {biggest_elf}, Value: {biggest_val}")