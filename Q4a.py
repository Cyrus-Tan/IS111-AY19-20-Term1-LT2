def store_family_relations(family_file):
    """returns a dictionary to store all the parent-child relations found in the file."""
    final_dict = {}
    data = open(family_file)
    for line in data:
        father_name = ""
        mother_name = ""
        line = line.rstrip()                                       # remove '\n' char at the end of each line---> to remove empty lines
        list_for_each_line = line.split(':')
        tuple_for_parents = list_for_each_line[0]
        list_for_tuple_for_parents = list(tuple_for_parents)
        tuple_for_children = list_for_each_line[1]
        list_for_each_children = tuple_for_children.split(';')     # gets a list for tuple of children and their gender
        # Loop through each char, append char if not ',', '(', ')' to get father and mother names
        have_not_reached_comma = True               # create flag variable which will change when reached comma
        for each_char in list_for_tuple_for_parents:
            if each_char == ',':                 # if char is comma, change flag_variable to True
                have_not_reached_comma = False
            if have_not_reached_comma == True and each_char.isalpha() == True:          # while True (have not reached comma)
                father_name += each_char                                                # if is alphabet and haven't reach comma--> will be father's name
            if have_not_reached_comma == False and each_char.isalpha() == True:     # have reached comma:
                mother_name += each_char         # if alphabet alrdy passed comma--> will be mother's name
        # Get Children names and their gender
        for each_child in list_for_each_children:
            second_flag_variable = True           # Create second flag_variable that checks if char has reached comma yet
            each_child = list(each_child)        # get a list of char for the entire list
            name_of_child = ""
            gender_of_child = ""
            for each_char in each_child:
                if each_char == ',':
                    second_flag_variable = False
                if second_flag_variable == True and each_char.isalpha() == True:   # have not reached comma and is alphabet--> name of child
                    name_of_child += each_char
                elif second_flag_variable == False and each_char.isalpha() == True:  # will be gender of child
                    gender_of_child += each_char

                # Check if gender is male or female
            if gender_of_child == 'M':
                relationship_of_child = 'son'
            else:
                relationship_of_child = 'daughter'
            # Start creating key-value pairs for the dict for father-child and mother-child pairs, and whether is son/daughter
            final_dict[father_name, name_of_child] = 'father'
            final_dict[mother_name, name_of_child] = 'mother'
            final_dict[name_of_child, father_name] = relationship_of_child
            final_dict[name_of_child, mother_name] = relationship_of_child
    return final_dict

print(store_family_relations('family_file.txt'))