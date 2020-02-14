def get_data(file):
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))
    return data


def parameters(data, instruction, index, relative_base):
    # param1
    if int(instruction[2]) == 0:
        para1 = data[index + 1]
    elif int(instruction[2]) == 1:
        para1 = index + 1
    elif int(instruction[2]) == 2:
        para1 = relative_base + data[index + 1]

    # param2
    if int(instruction[1]) == 0:
        para2 = data[index + 2]
    elif int(instruction[1]) == 1:
        para2 = index + 2
    elif int(instruction[1]) == 2 :
        para2 = relative_base + data[index + 2]

    # param3
    if int(instruction[0]) == 0:
        para3 = data[index + 3]
    elif int(instruction[0]) == 1 :
        para3 = index + 3
    elif int(instruction[0]) == 2:
        para3 = relative_base + data[index + 3]

    return para1, para2, para3


def intcode_computer(intcodes, input_value):
    index = 0
    input_counter = 0
    relative_base = 0
    output = 0
    new_base = 0
    while index < len(intcodes) -1:
        instruction = "%05d" % intcodes[index]
        opcode = int(instruction[3:])
        param1, param2, param3 = parameters(intcodes, instruction, index, relative_base)
        if opcode == 1:
            intcodes[param3] = intcodes[param1] + intcodes[param2]
            index += 4
        elif opcode == 2:
            intcodes[param3] = intcodes[param1] * intcodes[param2]
            index += 4
        elif opcode == 3:
            intcodes[param1] = input_value
            index += 2
        elif opcode == 4:
            output = intcodes[param1]
            print('Output at opcode 4', output)
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
        elif opcode == 9:
            relative_base += intcodes[param1]
            index += 2
        elif opcode == 99:
            return output


int_codes = get_data('input')
padding = [0] * 10000000
int_codes += padding
print('Part 1 - Final output: ', intcode_computer(int_codes, 1))
print('Part 2 - Final output: ', intcode_computer(int_codes, 2))

