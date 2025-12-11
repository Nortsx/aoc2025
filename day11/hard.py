from functools import cache
graph_nodes = {}
paths = []
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        labels_paths = line.split(':')
        node_paths = labels_paths[1].strip().split(' ')
        graph_nodes[labels_paths[0]] = node_paths

@cache
def look_for_path(node, end_node) -> int:
    if node == 'out':
        if end_node == 'out':
            return 1
        return 0
    if node == end_node:
        return 1

    path_sum = 0
    for path_node in graph_nodes[node]:
        path_sum += look_for_path(path_node, end_node)

    return path_sum

svr_fft = look_for_path('svr','fft')
fft_dac = look_for_path('fft','dac')
dac_out = look_for_path('dac','out')

svr_dac = look_for_path('svr','dac')
dac_fft = look_for_path('dac','fft')
fft_out = look_for_path('fft','out')

result = svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out
print(result)