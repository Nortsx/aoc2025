graph_nodes = {}

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        labels_paths = line.split(':')
        paths = labels_paths[1].strip().split(' ')
        graph_nodes[labels_paths[0]] = paths

def look_for_path(node):
    if node == 'out':
        return 1

    sum = 0
    for path in graph_nodes[node]:
        sum += look_for_path(path)

    return sum

print(look_for_path('you'))