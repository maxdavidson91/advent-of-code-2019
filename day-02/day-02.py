def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data


def part_one(noun, verb):
    data = get_data('input')
    data[1] = noun
    data[2] = verb
    index = 0
    for num in data[::4]:
        if num == 1:
            addition = data[data[index + 1]] + data[data[index + 2]]
            position = data[index + 3]
            data[position] = addition
        elif num == 2:
            multiplication = data[data[index + 1]] * data[data[index + 2]]
            position = data[index + 3]
            data[position] = multiplication
        elif num == 99:
            break
        index += 4
    return data[0]


def part_two(output):
    for x in range(100):
        for y in range(100):
            if part_one(x, y) == output:
                return 100 * x + y


print(part_one(12, 2))
print(part_two(19690720))
