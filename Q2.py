def get_longer_words(file_name):
    final_list = []
    data = open(file_name)
    for each_line in data:
        each_line = each_line.rstrip()     # remove '\n' character at end of each line
        each_line_splitted_as_list = each_line.split('&')
        for index in range(len(each_line_splitted_as_list)):
            if index != len(each_line_splitted_as_list) - 1:   # if not at last string
                if len(each_line_splitted_as_list[index+1]) > len(each_line_splitted_as_list[index]):
                    longer_string = each_line_splitted_as_list[index+1]
                else:
                    longer_string = each_line_splitted_as_list[index]
                final_list.append(longer_string)
    return final_list

#print(get_longer_words('q2_input_1.txt'))
print(get_longer_words('q2_input_2.txt'))