from shapely.geometry import Point, Polygon
with open('input.txt', 'r') as f:
    corner_coords = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)

def in_grid(corner_one, corner_two, polygon):
    min_x = min(corner_one[0], corner_two[0])
    max_x = max(corner_one[0], corner_two[0])
    min_y = min(corner_one[1], corner_two[1])
    max_y = max(corner_one[1], corner_two[1])


    left_upper_corner = Point(min_x, min_y)
    left_lower_corner = Point(min_x, max_y)
    right_lower_corner = Point(max_x, max_y)
    right_upper_corner = Point(max_x, min_y)
    compare_poly = Polygon([left_upper_corner, left_lower_corner, right_lower_corner, right_upper_corner, left_upper_corner])
    return polygon.covers(compare_poly)


corner_coords.append(corner_coords[0])
poly = Polygon(corner_coords)

max_area = 0
for i in range(len(corner_coords) - 1):
    for j in range(i+1, len(corner_coords)):
        if in_grid(corner_coords[i], corner_coords[j], poly):
            max_area = max(max_area, area(corner_coords[i], corner_coords[j]))

