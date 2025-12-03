with open('input.txt', 'r') as f:
    arrays = [line.strip() for line in f.readlines()]


def find_biggest_joltage(batteries):
    batteries = [int(char) for char in batteries.strip()]
    maxFirstNum = -1
    maxIdx = -1
    for i in range(len(batteries) -1):
        if batteries[i] > maxFirstNum:
            maxFirstNum = batteries[i]
            maxIdx = i
    maxLastNum = -1
    for j in range(maxIdx + 1, len(batteries)):
        if batteries[j] > maxLastNum:
            maxLastNum = batteries[j]
    return maxFirstNum*10 + maxLastNum

sum = 0
for battery in arrays:
  sum += find_biggest_joltage(battery)

print(sum)