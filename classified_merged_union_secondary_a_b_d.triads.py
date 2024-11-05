file_path = 'alter_union_secondary_a_b_d.triads'
output_file_path = 'merged_union_secondary_a_b_d.triads'
output_file_path_less_than_three_t = 'merged_union_secondary_a_b_d_less_than_three_t.triads'

all_char_sets = []

with open(file_path, 'r') as file:
    for line in file:
        char_set = set(line.strip().split(','))
        all_char_sets.append(char_set)

def merge_list(L):
    length = len(L)
    for i in range(1, length):
        for j in range(i):
            if L[i].isdisjoint(L[j]):
                continue
            x = L[i].union(L[j])
            L[i] = x
            L[j] = {0}
    return [i for i in L if i != {0}]

with open(output_file_path, 'w') as output_file, open(output_file_path_less_than_three_t, 'w') as output_file_less_than_three_t:
    for s in merge_list(all_char_sets):
        line = ','.join(s) + '\n'
        t_count = sum(1 for char in line if char == 'T')
        if t_count > 3:
            output_file.write(line)
        else:
            output_file_less_than_three_t.write(line)
