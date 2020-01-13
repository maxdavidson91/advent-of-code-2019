from itertools import permutations

def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data


def parameters(data, instruction, index):
    # param1
    if int(instruction[2]) == 0:
        para1 = data[index + 1]
    else:
        para1 = index + 1

    # param2
    if int(instruction[1]) == 0:
        para2 = data[index + 2]
    else:
        para2 = index + 2

    # param3 - need to use try as para3 may not exist
    try:
        if int(instruction[0]) == 0:
            para3 = data[index + 3]
        else:
            para3 = index + 3
    except: IndexError; para3 = None

    return para1, para2, para3


def intcode_computer(intcodes):
    index = 0
    while index < len(intcodes):
        instruction = "%05d" % intcodes[index]
        opcode = int(instruction[3:])
        param1, param2, param3 = parameters(intcodes, instruction, index)
        if opcode == 1:
            intcodes[param3] = intcodes[param1] + intcodes[param2]
            index += 4
        elif opcode == 2:
            intcodes[param3] = intcodes[param1] * intcodes[param2]
            index += 4
        elif opcode == 3:
            intcodes[param1] = yield
            index += 2

        if opcode == 4 or opcode == 99:
            if intcodes[param1] != 0 and intcodes[index + 2] == 99:
                yield intcodes[param1]
                break

            elif intcodes[param1] != 0 and intcodes[index + 2] != 99:
                yield intcodes[param1]
                # break
            else:
                break
            index += 2
        elif opcode == 5:
            if intcodes[param1] != 0:
                index = intcodes[param2]
            else:
                index += 3
        elif opcode == 6:
            if intcodes[param1] == 0:
                index = intcodes[param2]
            else:
                index += 3
        elif opcode == 7:
            if intcodes[param1] < intcodes[param2]:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            index += 4
        elif opcode == 8:
            if intcodes[param1] == intcodes[param2]:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            index += 4


intcodes = get_data('input')

max_thrusters = []
for phase_settings in permutations([5, 6, 7, 8, 9]):
    amplifiers = []
    for setting in phase_settings:
        generator = intcode_computer(intcodes)
        next(generator)
        generator.send(setting)
        amplifiers.append(generator)
        output = 0
    while True:
        for generator in amplifiers:
            output = generator.send(output)
            max_thrusters.append(output)
        try:
            for generator in amplifiers:
                next(generator)
        except:
            break

print("Part 2:", max(max_thrusters))
