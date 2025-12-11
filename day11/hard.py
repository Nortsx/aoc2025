graph_nodes = {}
paths = []
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        labels_paths = line.split(':')
        node_paths = labels_paths[1].strip().split(' ')
        graph_nodes[labels_paths[0]] = node_paths

print(graph_nodes)

def look_for_path(node, path_taken):
    if node == 'out':
        paths.append(path_taken)
        return

    path_to_follow = path_taken.copy()
    path_to_follow.append(node)
    for path_node in graph_nodes[node]:
        look_for_path(path_node,path_to_follow)

look_for_path('svr', [])

result = 0

for path in paths:
    found_fft = False
    found_dac = False
    for node in path:
        if node == 'fft':
            found_fft = True
        if node == 'dac':
            found_dac = True
    if found_fft and found_dac:
        result += 1

print(result)