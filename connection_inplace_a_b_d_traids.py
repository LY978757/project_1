file1_path = 'alter_mounted_filter_by_alter_string_a_b_d_triads_a_b_d_core_triads_function_block_strategy.one2many_gt41.25'
file2_path = 'a_b_d.triads'
output_path = 'a_b_d_triads_inplace_set'

file1_dict = {}
with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        key1 = tuple(columns[1:4])
        value1 = columns[0]
        if key1 not in file1_dict:
            file1_dict[key1] = []
        file1_dict[key1].append(value1)

file2_list = []
with open(file2_path, 'r') as file2:
    for line in file2:
        columns = line.strip().split('\t')
        char2_set = set(columns[0:3])
        file2_list.append(char2_set)

with open(output_path, 'w') as output_file:
    for char in file2_list:
        for key1, value1 in file1_dict.items():
            if char.intersection(set(value1)) and len(char.intersection(set(value1))) >= 2:
                output_file.write('{}\t{}'.format('\t'.join(char), '\t'.join(key1)))
