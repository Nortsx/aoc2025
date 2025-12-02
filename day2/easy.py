with open('input.txt', 'r') as f:
    line = f.readline().strip()
    values = line.split(',')

print(values)

def check_repeating(number) -> bool:
    num_str = str(number)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        return num_str[:mid] == num_str[mid:]
    return False

sum = 0
for value in values:
    range_vals = value.split('-')
    left_range = int(range_vals[0])
    right_range = int(range_vals[1])
    for i in range(left_range, right_range + 1):
        if check_repeating(i):
            sum += i

print(sum)