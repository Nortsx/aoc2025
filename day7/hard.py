from functools import cache

with open('input.txt', 'r') as f:
    space = [list(line.strip()) for line in f.readlines()]
    print(space)

beams = [(space[0].index('S'), 0)]
memo = {}

@cache
def count_beam(beam) -> int:
    if beam[1] >= len(space)-1:
        return 1
    if space[beam[1]][beam[0]] != '.':
        return count_beam((beam[0]+1, beam[1])) + count_beam((beam[0]-1, beam[1]))
    else:
        return count_beam((beam[0], beam[1]+1))

print(count_beam((space[0].index('S'), 0)))
