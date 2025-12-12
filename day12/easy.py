figures = [
    [['#','.','#'],['#','.','#'],['#','#','#']],
    [['#','#','#'],['#','#','.'],['#','#','.']],
    [['#','#','#'],['#','#','.'],['#','.','.']],
    [['.','.','#'],['.','#','#'],['#','#','.']],
    [['#','.','#'],['#','#','#'],['#','.','#']],
    [['.','#','#'],['#','#','#'],['#','.','#']],
]

def get_shape_size(shape):
    sum = 0
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == '#':
                sum += 1

    return sum

spaces = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        data_set = line.strip().split(':')
        space_size = data_set[0]
        space_present_list = [int(x) for x in data_set[1].strip().split(' ')]
        spaces.append((space_size, space_present_list))

unfit = 0
for idx, space in enumerate(spaces):
    size = int(space[0].split("x")[0])*int(space[0].split("x")[1])
    presents = space[1]
    potential_size = 0
    for i in range(len(presents)):
        potential_size += presents[i] * get_shape_size(figures[i])
    if potential_size > size:
        unfit += 1
        print("NOT FIT ", idx)

print(len(spaces) - unfit)