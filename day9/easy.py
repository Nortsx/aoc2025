with open('input.txt', 'r') as f:
    corner_coords = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

max_area = 0
for i in range(len(corner_coords) - 1):
    for j in range(i+1, len(corner_coords)):
        max_area = max(max_area, area(corner_coords[i], corner_coords[j]))

print(max_area)