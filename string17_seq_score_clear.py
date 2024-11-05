file1_path = 'b_d.RBH'
file2_path = 'd_b.one2many'
output_path = 'd_b.one_to_many'

column1_set = set()
column2_set = set()

with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        if len(columns) >= 2:
            column1_set.add(columns[0])
            column2_set.add(columns[1])

mismatching_lines = []

with open(file2_path, 'r') as file2:
    for line in file2:
        columns = line.strip().split('\t')
        if len(columns) >= 2 and columns[0] not in column1_set and columns[0] not in column2_set \
                and columns[1] not in column1_set and columns[1] not in column2_set:
            mismatching_lines.append(line.strip())

with open(output_path, 'w') as output_file:
    output_file.write('\n'.join(mismatching_lines))