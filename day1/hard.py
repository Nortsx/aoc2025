with open('input.txt', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]


def rotate(direction, rotate_for, prev_value) -> (int, int):
    crossings = rotate_for // 100
    real_rotation = rotate_for % 100
    new_value = prev_value
    if direction == 'L':
        new_value = prev_value - real_rotation
        if new_value < 0:
            new_value += 100
            if prev_value != 0:
                crossings += 1
    if direction == 'R':
        new_value = prev_value + real_rotation
        if new_value > 100:
            new_value -= 100
            if prev_value != 0:
                crossings += 1
        elif new_value == 100:
            new_value = 0
    return new_value, crossings


pos = 50
zeros = 0
for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    pos, crossings = rotate(direction, distance, pos)
    if pos == 0:
        zeros += 1
    zeros += crossings

print(zeros)