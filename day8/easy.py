import math

with open('input.txt', 'r') as f:
    capacitors = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def distance(a, b) -> float:
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))

circuits = []
distances = []

for i in range(len(capacitors)-1):
    for j in range(i+1, len(capacitors)):
        dist = distance(capacitors[i], capacitors[j])
        distances.append((dist, i, j))

distances.sort()

connections_made = 0
for dist, i, j in distances:
    circuits_to_merge = []
    for circuit in circuits:
        if i in circuit or j in circuit:
            circuits_to_merge.append(circuit)

    if len(circuits_to_merge) == 0:
        circuits.append({i, j})
    elif len(circuits_to_merge) == 1:
        circuits_to_merge[0].add(i)
        circuits_to_merge[0].add(j)
    else:
        merged = set()
        for circuit in circuits_to_merge:
            merged.update(circuit)
            circuits.remove(circuit)
        merged.add(i)
        merged.add(j)
        circuits.append(merged)

    connections_made += 1
    if connections_made >= len(capacitors):
        break

print(circuits)
sum = 1
counter = 0
for i in sorted(circuits, key=len, reverse=True):
    sum *= len(i)
    counter += 1
    if counter >= 3:
        break

print(sum)

