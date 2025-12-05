with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]
    intervals = [(int(interval.split('-')[0]), int(interval.split('-')[1])) for interval in input[:input.index('')]]

intervals.sort(key=lambda x: x[0])
merged = []

sum = 0
for start, end in intervals:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    sum += end - start + 1

print(sum)