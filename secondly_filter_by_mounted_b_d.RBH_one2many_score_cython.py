file1_path = 're_all_merged_alter_string_filter_by_mounted_a_b_d.RBH_one2many_score_cython_gt70'
file2_path = 'filter_by_mounted_b_d.RBH_one2many_score_cython'
output_path = 'secondly_filter_by_mounted_b_d.RBH_one2many_score_cython'

all_char_sets = set()

with open(file1_path, 'r') as file1:
    for line in file1:
        char_set = set(line.strip().split(','))
        all_char_sets.update(char_set)

mismatching_lines = []

with open(file2_path, 'r') as file2:
    for line in file2:
        columns = line.strip().split('\t')
        if columns[0] not in all_char_sets and columns[1] not in all_char_sets:
            mismatching_lines.append(line.strip())

with open(output_path, 'w') as output_file:
    output_file.write('\n'.join(mismatching_lines))
