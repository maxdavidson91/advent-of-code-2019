def get_data(file):
    with open(file, 'r') as f:
        data = f.readline().strip()
    return data


digits = get_data('input.txt')
height = 6
width = 25
layer_len = width * height

layers = []
for i in range(0, len(digits), layer_len):
    layers.append(digits[i:i + layer_len])

min_zero = min(layer.count('0') for layer in layers)
part_one = [layer.count('1') * layer.count('2') for layer in layers if layer.count('0') == min_zero]

print("Part one:", part_one[0])

# transpose the list of lists
image = list(map(list, zip(*layers)))

pixels = []
for column in image:
    for i in range(len(column)):
        if column[i] != '2':
            pixels.append(column[i])
            break

rows = []
for i in range(0, len(pixels), width):
    rows.append(pixels[i:i + width])
    
for row in rows:
    for i in row:
        if i == '1':
            print('#', end='')
        else: print(' ', end='')
    print('')
    
