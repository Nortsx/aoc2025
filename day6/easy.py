with open('input.txt', 'r') as f:
    input = [[x for x in line.strip().split(' ') if x != ''] for line in f.readlines()]

total = 0

first_line = input[0]
last_line = input[-1]

for i in range(len(first_line)):
    midsum = 0
    for j in range(len(input) - 1):
        if last_line[i] == '+':
            midsum += int(input[j][i])
        else:
            if midsum == 0:
                midsum = 1*int(input[j][i])
            else:
                midsum *= int(input[j][i])
    total += midsum

print(total)