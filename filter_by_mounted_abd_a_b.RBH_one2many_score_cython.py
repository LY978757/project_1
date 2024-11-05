file1_path = 'merged_all_a_b_d_triads_merged_alter_mounted_a_b_d_core_network_mathcing_triads.one2many_gt70_cython'
file2_path = 'a_b.one2many'
output_path = 'filter_by_mounted_a_b.RBH_one2many_score_cython'
# 用于去除已分类的联对基因、单基因
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
