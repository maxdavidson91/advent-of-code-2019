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


data = get_data('input')
index = 0
while index < len(data):
    instruction = "%05d" % data[index]
    opcode = int(instruction[3:])
    param1, param2, param3 = parameters(data, instruction, index)
    if opcode == 1:
        data[param3] = data[param1] + data[param2]
        index += 4
    elif opcode == 2:
        data[param3] = data[param1] * data[param2]
        index += 4
    elif opcode == 3:
        data[param1] = int(input("Please type your input:"))
        index += 2
    if opcode == 4 or opcode == 99:
        if data[param1] != 0 and data[index + 2] == 99:
            print(f"Test succeeded with final output: {data[param1]}")
            break
        elif data[param1] != 0 and data[index + 2] != 99:
            print(f"Test failed with output: {data[param1]}")
            break
        else:
            # output should be 0 for success
            print(f"Test succeeded with output: {data[param1]}")
        index += 2
    if opcode == 5:
        if data[param1] != 0:
            index = data[param2]
        else:
            index += 3
    if opcode == 6:
        if data[param1] == 0:
            index = data[param2]
        else:
            index += 3
    if opcode == 7:
        if data[param1] < data[param2]:
            data[param3] = 1
        else:
            data[param3] = 0
        index += 4
    if opcode == 8:
        if data[param1] == data[param2]:
            data[param3] = 1
        else:
            data[param3] = 0
        index += 4
