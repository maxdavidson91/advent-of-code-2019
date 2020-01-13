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

    # param3
    if int(instruction[0]) == 0:
        para3 = data[index + 3]
    else:
        para3 = index + 3

    return para1, para2, para3


def intcode_computer(intcodes, phase_setting, input_instruction):
    index = 0
    input_counter = 0
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
            if input_counter == 0:
                intcodes[param1] = phase_setting
            else:
                intcodes[param1] = input_instruction
            input_counter += 1
            index += 2
        if opcode == 4 or opcode == 99:
            if intcodes[param1] != 0 and intcodes[index + 2] == 99:
                print(f"Test succeeded with final output: {intcodes[param1]}")
                return intcodes[param1]
            elif intcodes[param1] != 0 and intcodes[index + 2] != 99:
                print(f"Test failed with output: {intcodes[param1]}")
                # print(opcode,param1,param2,param3)
                return intcodes[param1]
            else:
                # output should be 0 for success
                print(f"Test succeeded with output: {intcodes[param1]}")
                # return intcodes[param1]
            index += 2
        if opcode == 5:
            if intcodes[param1] != 0:
                index = intcodes[param2]
            else:
                index += 3
        if opcode == 6:
            if intcodes[param1] == 0:
                index = intcodes[param2]
            else:
                index += 3
        if opcode == 7:
            if intcodes[param1] < intcodes[param2]:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            index += 4
        if opcode == 8:
            if intcodes[param1] == intcodes[param2]:
                intcodes[param3] = 1
            else:
                intcodes[param3] = 0
            index += 4


#initial_codes = get_data('input')
int_codes = get_data('input')
thruster_signals = []
for i in permutations([0, 1, 2, 3, 4]):
    input_signal = 0
    for setting in range(0, 5):
        phase_setting = i[setting]
        output_signal = intcode_computer(int_codes, phase_setting, input_signal)
        input_signal = output_signal
    thruster_signals.append(input_signal)

print("Part 1:", max(thruster_signals))
