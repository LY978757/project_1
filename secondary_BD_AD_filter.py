file1_path = 'B_D.latest_score_gt70'
file2_path = 'filter_a_d.RBH_one2many_score_gt70'
output_path_1 = 'A_D.latest'
output_path_2 = 'B_D_1.latest'

column1_set = set()

with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        if len(columns) >= 2:
            column1_set.add(columns[1])

mismatching_lines_1 = []
with open(file2_path, 'r') as file2:
    for line in file2:
        columns = line.strip().split('\t')
        if len(columns) >= 2 and columns[1] in column1_set:
            mismatching_lines_1.append(line.strip())

with open(output_path_1, 'w') as output_file_1:
    output_file_1.write('\n'.join(mismatching_lines_1))

column2_set = set()
with open(output_path_1, 'r') as output_file_1:
    for line in output_file_1:
        columns = line.strip().split('\t')
        if len(columns) >= 2:
            column2_set.add(columns[1])

mismatching_lines_2 = []
with open(file1_path, 'r') as file1:
    for line in file1:
        columns = line.strip().split('\t')
        if len(columns) >= 2 and columns[1] in column2_set:
            mismatching_lines_2.append(line.strip())

with open(output_path_2, 'w') as output_file_2:
    output_file_2.write('\n'.join(mismatching_lines_2))

        

