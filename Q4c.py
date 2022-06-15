from Q4b import get_relation_through_link
def get_relation(family_dict, p1, p2):
    """returns the family relation between p1 and p2."""
    # Create empty list, and append the subsequent letter to it to find link from p1 to p2
    final_list = []
    list_of_related = []
    second_list_of_related = []
    third_list_of_related = []
    list_of_tuple_for_keys = list(family_dict.keys())          # get all possible tuple pair in list
    final_list.append(p1)                                      # add first person to final_list
    for each_tuple in list_of_tuple_for_keys:
        if each_tuple[0] == p1:
            list_of_related.append(each_tuple[1])              # add directly related pple of p1 to list

    for each_tuple in list_of_tuple_for_keys:
        if each_tuple[0] in list_of_related:                   # Check if first element in tuple is in list_of_related
            second_list_of_related.append(each_tuple[1])
            if each_tuple[1] == p2:
                final_list.append(each_tuple[0])               # Scenario 1: 3 people: add second person and last person
                final_list.append(p2)

    if final_list[-1] != p2:                            # if haven't reached p2
        for each_tuple in list_of_tuple_for_keys:
            if each_tuple[0] in second_list_of_related:
                third_list_of_related.append(each_tuple[1])
                if each_tuple[1] == p2:
                    # Find back second person/ third last person for 4 people
                    for individual_tuple in list_of_tuple_for_keys:
                        if individual_tuple[1] == each_tuple[0]:           # e.g: To find for 'B' which is second element in tuple
                            second_person = individual_tuple[0]
                            if second_person != p2:
                                final_list.append(second_person)           ## Get the second person for 4 people list
                    # Scenario 2: add second last person and last person
                    final_list.append(each_tuple[0])
                    final_list.append(p2)
    # Use the function created in 4b to get output
    return get_relation_through_link(family_dict=family_dict, link=final_list)

print(get_relation({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter',
                    ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, 'A', 'C'))
print(get_relation({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter',
                 ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, 'C', 'A'))
print(get_relation({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter',
                    ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, 'B', 'D'))
print(get_relation({('A', 'B') : 'father', ('B', 'A') : 'son', ('B', 'C') : 'father', ('C', 'B') : 'daughter',
                    ('D', 'C') : 'mother', ('C', 'D') : 'daughter'}, 'D', 'A'))

# LEFTOVER ISSUE: How to re-iterate over the list multiple times        (SOLVED, but can be better)
#               ---> Need to get a list(which will be link) of relationship from p1 to p2 (but len(list) < 5)
#               ---> Can't find second person to add if there's 4 people in list
#               ---> Create a function with parameter that decides if i need to add the choide of including second person (when there's 4 people)