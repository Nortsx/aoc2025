with open('input.txt', 'r') as f:
    space = [list(line.strip()) for line in f.readlines()]
    print(space)

beams = [(space[0].index('S'), 0)]

current_step = 0
splits = 0
while True:
    current_step += 1
    new_beams = set()
    for beam in beams:
        if space[beam[1]+1][beam[0]] == '^':
            splits += 1
            new_beams.add((beam[0]+1, beam[1]+1))
            new_beams.add((beam[0]-1, beam[1]+1))
        else:
            new_beams.add((beam[0], beam[1]+1))
    beams = new_beams
    # print(current_step)
    # print(len(beams))
    if current_step == len(space)-1:
        break

print(splits)