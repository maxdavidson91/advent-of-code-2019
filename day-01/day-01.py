with open('input', 'r') as f:
    data = f.read().splitlines()


def fuel_calc(mass):
    fuel = int(int(mass)/3) - 2
    return fuel


def part_one(numbers):
    fuel = sum(fuel_calc(line) for line in numbers)
    return fuel


def part_two(numbers):
    fuel_requirements = []
    for line in numbers:
        new_fuel = fuel_calc(line)
        total_fuel = 0
        while new_fuel > 0:
            total_fuel += new_fuel
            new_fuel = fuel_calc(new_fuel)
        fuel_requirements.append(total_fuel)
    return sum(fuel_requirements)


print(part_one(data))
print(part_two(data))
