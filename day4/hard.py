with open('input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]



def can_access(grid, pos):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]
    other_rolls = 0
    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue
        if grid[y][x] == '@':
            other_rolls += 1

    return other_rolls < 4


total_removed = 0
while True:
    removed_this_round = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                if can_access(grid, (x, y)):
                    removed_this_round += 1
                    grid[y][x] = '.'
    total_removed += removed_this_round
    if removed_this_round == 0:
        break

print(total_removed)