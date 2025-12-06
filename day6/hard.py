with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

operations = [x for x in lines[-1].strip().split(' ') if x != '']

current_number = ''
current_operation_idx = 0
number_found = False
biggest_line_len = (max(len(line) for line in lines))
total = 0
midsum = 0
for i in range(biggest_line_len):
    number_found = False
    for j in range(len(lines) - 1):
        if len(lines[j]) > i and lines[j][i] not in ' ':
            current_number += lines[j][i]
            number_found = True
    if number_found:
        # print(current_number)
        if operations[current_operation_idx] == '+':
            midsum += int(current_number)
        else:
            if midsum == 0:
                midsum = 1*int(current_number)
            else:
                midsum *= int(current_number)
    else:
        # print(midsum)
        total += midsum
        current_operation_idx += 1
        midsum = 0
    current_number = ''
total += midsum
print(total)