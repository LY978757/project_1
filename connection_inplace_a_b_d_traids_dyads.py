file1_path = 'alter_mounted_filter_by_triads_dyads_set.one2many_gt41.25'
file2_path = 'a_b_d.triads_dyads'
output1_path = 'a_b_d_triads_dyads_inplace_set'

file1_dict = {}
file2_dict = {}
with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        if len(columns) >= 4:
            key1 = tuple(columns[1:4])
            value1 = columns[0]
            if key1 not in file1_dict:
                file1_dict[key1] = []
            file1_dict[key1].append(value1)
        elif len(columns) == 3:
            key2 = tuple(columns[1:3])
            value2 = columns[0]
            if key2 not in file2_dict:
                file2_dict[key2] = []
            file2_dict[key2].append(value2)
print(file2_dict)

file3_list = []
with open(file2_path, 'r') as file2:
    for line in file2:
        columns = line.strip().split('\t')
        char2_set = set(columns)
        file3_list.append(char2_set)


with open(output1_path, 'w') as output_file1:
    for char in file3_list:
        for key1, value1 in file1_dict.items():
            if char.intersection(set(value1)) and len(char.intersection(set(value1))) >= 2:
                output_file1.write('{}\t{}\n'.format('\t'.join(char), '\t'.join(key1)))
        for key2, value2 in file2_dict.items():
            if len(char) >= 3 and len(char.intersection(set(value2))) == 3:
                output_file1.write('{}\t{}\n'.format('\t'.join(char), '\t'.join(key2)))
            elif len(char) == 2 and len(char.intersection(set(value2))) == 2:
                output_file1.write('{}\t{}\n'.format('\t'.join(char), '\t'.join(key2)))

