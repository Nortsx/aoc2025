with open('input.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]
    ingredients = input[input.index('')+1:]
    intervals = input[:input.index('')]

intervals = [(int(interval.split('-')[0]), int(interval.split('-')[1])) for interval in intervals]
ingredients = [int(ingredient) for ingredient in ingredients]


print(intervals)
print(ingredients)

freshNum = 0

for ingredient in ingredients:
    for interval in intervals:
        if interval[0] <= ingredient <= interval[1]:
            freshNum += 1
            break

print(freshNum)