with open('input.txt', 'r') as f:
    corner_coords = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def in_grid(corner_one, corner_two, grid):
    left_upper_corner = [min(corner_one[0], corner_two[0]), min(corner_one[1], corner_two[1])]
    left_lower_corner = [min(corner_one[0], corner_two[0]), max(corner_one[1], corner_two[1])]
    right_lower_corner = [max(corner_one[0], corner_two[0]), max(corner_one[1], corner_two[1])]
    right_upper_corner = [max(corner_one[0], corner_two[0]), min(corner_one[1], corner_two[1])]
    return grid[left_upper_corner[1]][left_upper_corner[0]] in ['X', '#'] and grid[left_lower_corner[1]][left_lower_corner[0]] in ['X', '#'] and grid[right_lower_corner[1]][right_lower_corner[0]] in ['X', '#'] and grid[right_upper_corner[1]][right_upper_corner[0]] in ['X', '#']

# Find actual bounds of coordinates to create minimal grid
min_x = min(coord[0] for coord in corner_coords)
max_x = max(coord[0] for coord in corner_coords)
min_y = min(coord[1] for coord in corner_coords)
max_y = max(coord[1] for coord in corner_coords)

width = max_x - min_x + 1
height = max_y - min_y + 1

print(f"Grid size: {width} x {height} (instead of 100K x 100K)")


grid = [['.' for _ in range(width)] for _ in range(height)]


# Offset coordinates to fit in the smaller grid
offset_coords = [[coord[0] - min_x, coord[1] - min_y] for coord in corner_coords]
# for corner in corner_coords:
#     grid[corner[1]][corner[0]] = '#'
# print("filled corners")
# for i in range(len(corner_coords) - 1):
#     for j in range(i+1, len(corner_coords)):
#         if corner_coords[i][1] == corner_coords[j][1]:
#             for fill_x in range(min(corner_coords[i][0], corner_coords[j][0]) + 1, max(corner_coords[i][0], corner_coords[j][0])):
#                 grid[corner_coords[i][1]][fill_x] = 'X'
#         if corner_coords[i][0] == corner_coords[j][0]:
#             for fill_y in range(min(corner_coords[i][1], corner_coords[j][1]) + 1, max(corner_coords[i][1], corner_coords[j][1])):
#                 grid[fill_y][corner_coords[i][0]] = 'X'
#
# print("filled lines between corners")
#
# # Bucket fill - flood fill from outside, then fill interior
# def flood_fill_exterior(grid):
#     """Mark all cells reachable from the edges that are not enclosed"""
#     rows = len(grid)
#     cols = len(grid[0])
#     visited = set()
#     stack = []
#
#     for y in range(rows):
#         if grid[y][0] == '.':
#             stack.append((y, 0))
#         if grid[y][cols - 1] == '.':
#             stack.append((y, cols - 1))
#     for x in range(cols):
#         if grid[0][x] == '.':
#             stack.append((0, x))
#         if grid[rows - 1][x] == '.':
#             stack.append((rows - 1, x))
#
#     while stack:
#         y, x = stack.pop()
#         if y < 0 or y >= rows or x < 0 or x >= cols:
#             continue
#         if (y, x) in visited:
#             continue
#         if grid[y][x] in ['#', 'X']:
#             continue
#
#         visited.add((y, x))
#         grid[y][x] = 'O'  # Mark as outside
#
#         stack.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
#
# flood_fill_exterior(grid)
# print("flood filled exterior")
# # Fill all remaining '.' cells with 'X' (they're interior)
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == '.':
#             grid[y][x] = 'X'
# print("replaced with X")
#
# # print_grid(grid)
# max_area = 0
# for i in range(len(corner_coords) - 1):
#     for j in range(i+1, len(corner_coords)):
#         if in_grid(corner_coords[i], corner_coords[j], grid):
#             max_area = max(max_area, area(corner_coords[i], corner_coords[j]))
#
# print(max_area)