with open('input.txt', 'r') as f:
    line = f.readline().strip()
    values = line.split(',')

print(values)

def check_repeating(number) -> bool:
    num_str = str(number)
    mid = len(num_str) // 2
    for potential_length in range(1,mid+1):
        if len(num_str) % potential_length == 0:
            chunks = [num_str[i:i+potential_length] for i in range(0, len(num_str), potential_length)]
            if all(chunk == chunks[0] for chunk in chunks):
                return True
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