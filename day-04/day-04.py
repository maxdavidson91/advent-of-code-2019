lower = 347312
upper = 805915

passwords = [sorted(str(i)) for i in range(lower, upper)]
passwords = sorted([''.join(i) for i in passwords])

unique = []
for i in passwords:
    if i not in unique and (len(set(i)) != len(i)):
        if lower <= int(i) <= upper:
            unique.append(i)

print('Part 1: ', len(unique))

new_list = []
for i in unique:
    for num in i:
        if i.count(num) == 2 and i not in new_list:
            new_list.append(i)

print('Part 2: ', len(new_list))
