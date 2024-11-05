file3_path = 'file3.txt'
file4_path = 'file4.txt'
output_path = 'output.txt'

file3_dict = {}
with open('file3.path', 'r') as file3:
    for line in file3:
        columns = line.strip().split('\t')
        if len(columns) == 2:
            file3_dict[columns[0]] = columns[1]

file4_dict = {}
with open('file4.path', 'r') as file4:
    for line in file4:
        colums = line.strip().split('\t')
        if len(colums) == 2:
            file4_dict[columns[1]] = columns[0]

matching_dict = {}
for key3, value3 in file3_dict.items():
    if key3 in file4_dict:
        matching_dict[key3] = (value3, file4_dict[key3]) 
 
with open(output_path, 'w') as output_file:
    for key3, (value3, value4) in matching_dict.items():
        if value3 == value4:
            output_file.write(f'{key3}\t{value3}\t{value4}\n')


