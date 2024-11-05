
file1_path = 'file1.txt'
dict1 = {}
with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        key = columns[0]
        value = columns[1]
        if key in dict1:
            dict1[key].append(value)
        else:
            dict1[key] = [value]

reverse_dict = {}
for key, values in dict1.items():
    for value in values:
        if value not in reverse_dict:
            reverse_dict[value] = [key]
        elif key not in reverse_dict[value]:
            reverse_dict[value].append(key)

output_path = 'output.txt'
with open(output_path, 'w') as output_file:
    for key, values in dict1.items():
        keys = []
        for value in values:
            if value in reverse_dict:
                keys.extend(reverse_dict[value])
        keys_str = ', '.join(set(keys))


    line = f'{values_str}\t{keys_str}\n'

    if line not in written_lines:
            output_file.write(line)
            written_lines.add(line)


        
        