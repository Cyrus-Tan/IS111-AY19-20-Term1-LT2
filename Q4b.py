def get_relation_through_link(family_dict, link):
    """returns the family relation between the first person in link and the last person in link"""
    final_output = ""
    new_first_relationship = ""
    # Find possibilities of number of elements, how many r/s
    if len(link) == 2:               # if only two elements
        first_person = link[0]
        last_person = link[1]
        final_output += family_dict[first_person, last_person]
    elif len(link) == 3:             # if has 3 elements
        first_person = link[0]
        second_person = link[1]
        last_person = link[2]
        first_relationship = family_dict[first_person, second_person]
        second_relationship = family_dict[second_person, last_person]
    elif len(link) == 4:             # if has 4 elements
        first_person = link[0]
        second_person = link[1]
        third_person = link[2]
        last_person = link[3]
        first_relationship = family_dict[first_person, second_person]
        second_relationship = family_dict[second_person, third_person]
        third_relationship = family_dict[third_person, last_person]
    # Access the text file
    data = open('relation_mapping.txt')
    repeat_loop = True                        # Create flag variable
    while repeat_loop:
        for each_line in data:
            each_line = each_line.rstrip()         # remove '\n' char at end of each line
            each_line = each_line.split(":")
            first_and_second_relationship = each_line[0]
            # get the first and second r/s separated based on comma
            first_and_second_relationship_list = list(first_and_second_relationship)   # Convert to a list of individual chars
            first_relationship_name = ""                 # create empty string for me to append char afterwards
            second_relationship_name = ""
            have_not_reached_comma = True                # create flag variable that will change after char reaches comma
            for each_char in first_and_second_relationship_list:
                if each_char == ",":
                    have_not_reached_comma = False
                if each_char.isalpha() == True and have_not_reached_comma == True:
                    first_relationship_name += each_char                     # will be for first r/s
                elif each_char.isalpha() == True and have_not_reached_comma == False:
                    second_relationship_name += each_char                    # will be for second r/s

            # Now compare the r/s between family_dict and the text file
            if len(link) < 4:     # if link list has only 3 or less elements
                final_relationship = each_line[1]
                if first_relationship == first_relationship_name and second_relationship == second_relationship_name:
                    final_output += final_relationship
                    repeat_loop = False                    # end the while loop
            elif len(link) == 4:  # if link list has 4 elements
                if first_relationship == first_relationship_name and second_relationship == second_relationship_name:
                    new_first_relationship += each_line[1]              # new_first_relationship will be the new first_relationship_name
            if new_first_relationship == first_relationship_name and third_relationship == second_relationship_name:
                final_relationship = each_line[1]
                final_output += final_relationship
                repeat_loop = False                        # end the while loop
    return final_output


#print(get_relation_through_link({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter', ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, ['A', 'B', 'C']))
#print(get_relation_through_link({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter', ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, ['C', 'B', 'A'],))
#print(get_relation_through_link({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter', ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, ['B', 'C', 'D']))
#print(get_relation_through_link({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter', ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, ['D', 'C', 'B', 'A']))