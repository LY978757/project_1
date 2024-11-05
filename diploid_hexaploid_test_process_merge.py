def merge(input_file_1, input_file_2, output_file):
    with open(input_file_1, 'r') as input_1, open(input_file_2, 'r') as input_2:

        dict_1 = {}
        dict_2 = {}
               
#header行名称
        header_1 = input_1.readline().strip().split('\t')
        header_2 = input_2.readline().strip().split('\t')[1:]

        
        header_3 = '\t'.join(header_1 + header_2)
#字典_1       
        for line in input_1:
            if line.strip():
                columns_1 = line.strip().split('\t')
                key_1 = columns_1[0]
                value_1 = columns_1[1:]
                if key_1 not in dict_1:
                    dict_1[key_1] = []
                dict_1[key_1].append(value_1)

#字典_2
        for line in input_2:
            if line.strip():
                columns_2 =line.strip().split('\t')
                key_2 = columns_2[0]
                value_2 = columns_2[1:]
                if key_2 not in dict_2:
                    dict_2[key_2] = []
                dict_2[key_2].append(value_2)
#字典补全
    with open(output_file, 'w') as output:

        output.write(header_3 + '\n')
        all_keys = set(dict_1.keys()).union(set(dict_2.keys()))
        for key in all_keys:
            value_1 = dict_1.get(key, ['0'] * len(header_1[1:]))
            value_2 = dict_2.get(key, ['0'] * len(header_2))

            f_value_1 = [item for sublist in value_1 for item in sublist]
            f_value_2 = [item for sublist in value_2 for item in sublist] 

            output.write(f'{key}\t' + '\t'.join(f_value_1) + '\t' + '\t'.join(f_value_2) + '\n')
                        
merge('vcf_diploid_landrace_D_all_variant', 'vcf_D_all_variant_test_process_del_LC_replace_number_header_test', 'vcf_diploid_landrace_cultivar_D_all_variant')
            