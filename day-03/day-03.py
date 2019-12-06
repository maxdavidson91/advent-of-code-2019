def get_data(file):
    with open(file, 'r') as f:
        wires = [f.split(',') for f in f.read().splitlines()]
    return wires


def draw_line(line):
    x_dict = {'L': -1, 'R': 1, 'D': 0, 'U': 0}
    y_dict = {'L': 0, 'R': 0, 'D': -1, 'U': 1}
    x, y = (0, 0)
    z = 0
    wire = {}
    for i in line:
        for step in range(int(i[1:])):
            x += x_dict[i[0]]
            y += y_dict[i[0]]
            z += 1
            wire[(x, y)] = z
    return wire


data = get_data('input')
line_one = draw_line(data[0])
line_two = draw_line(data[1])

intersections = line_one.keys() & line_two.keys()
part_one = min(abs(sum(i)) for i in intersections)
part_two = min((line_one[i] + line_two[i]) for i in intersections)
print(part_one)
print(part_two)
