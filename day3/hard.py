with open('input.txt', 'r') as f:
    arrays = [line.strip() for line in f.readlines()]


def find_biggest_joltage(batteries):
    batteries = [int(char) for char in batteries.strip()]
    current_joltage = 0
    prev_max_idx = -1
    for i in range(11, -1, -1):
        max_num = 0
        new_max_idx = -1
        for bat in range(prev_max_idx+1, len(batteries) - i):
            if max_num < batteries[bat]:
                new_max_idx = bat
                max_num = batteries[bat]
        prev_max_idx = new_max_idx
        current_joltage += max_num * pow(10, i)

    return current_joltage

sum = 0
for battery in arrays:
  sum += find_biggest_joltage(battery)

print(sum)