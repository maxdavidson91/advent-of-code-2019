def get_data(file):
    with open(file, 'r') as f:
        data = {x.split(')')[1]: x.split(')')[0] for x in f.read().splitlines()}
    return data


def path_to_planet(start, target):
    path = []
    planet = orbits[start]
    while orbits[target] not in path:
        planet = orbits[planet]
        if planet != orbits[target]:
            path.append(planet)
        if planet == 'COM':
            break
    return path


def min_distance(san, you):
    for x in san:
        for y in you:
            if x == y:
                return int(san_path.index(x) + 1 + you_path.index(y) + 1)


orbits = get_data('input')
orbit_count = 0
for i in orbits.keys():
    while i in orbits:
        orbit_count += 1
        i = orbits[i]

you_path = path_to_planet('YOU', 'SAN')
san_path = path_to_planet('SAN', 'YOU')

print('Part One:', orbit_count)
print('Part Two:', min_distance(san_path, you_path))
