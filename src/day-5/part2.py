from typing import Tuple, List, Union


def get_from_box(x: int, y: int, boxes: str) -> Union[None, str]:
    x_position = 1 + x * 4
    if boxes[y][x_position] == " ":
        return None
    return boxes[y][x_position]


def get_from_movements(movements) -> List[int]:
    moves = list()
    for move in movements:
        values = move.split()
        moves.append(
            [
                int(values[1]),
                int(values[3]) - 1,
                int(values[5]) - 1,
            ]
        )
    return moves


def read_boxes(boxes: str) -> Tuple[List[str]]:
    num_stacks = len(boxes[-1].split())
    max_box_height = len(boxes) - 1
    stacks = [list() for _ in range(num_stacks)]
    boxes = list(reversed(boxes))[1:]

    for j in range(max_box_height):
        for i in range(num_stacks):
            value_from_box = get_from_box(i, j, boxes)
            if value_from_box:
                stacks[i].append(value_from_box)
    return stacks


def main():

    with open("input.txt") as f:
        lines = f.read().split("\n")

    boxes = []
    movements = []

    for idx, line in enumerate(lines):
        if line == "":
            break
        boxes.append(line)
    for line in lines[idx + 1 :]:
        movements.append(line)
    stacks = read_boxes(boxes)
    movements = get_from_movements(movements)

    for move in movements:
        num_moves, start, end = move
        values = list()
        for _ in range(num_moves):
            values.append(stacks[start].pop())
        values = reversed(values)
        stacks[end].extend(values)

    final_result = ""
    for value in stacks:
        final_result += str(value[-1])
    print(final_result)


main()
