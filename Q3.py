def compute_total_price(price_dict, item_list):
    """returns the total price of the items in the item list based on the price information in the price dictionary."""
    total_price = 0
    for each_item_as_tuple in item_list:
        name_of_item = each_item_as_tuple[0]
        number_of_item = each_item_as_tuple[1]
        if name_of_item not in price_dict:              # if item cannot be found in price_dict, price of it will be 0
            price_of_item = 0
        else:
            price_of_item = price_dict[name_of_item]
        individual_total_price = number_of_item*price_of_item
        total_price += individual_total_price
    return "{:.1f}".format(total_price)                    # PYTHON STRING FORMATTING: round final total_cost to 2 d.p
                                                           # TAKE NOTE: after python string formatting, value shown in console is a string
                                                           # if want convert it to int----> must change str to float first, then to int
                                                           # REASON: you get a ValueError if you pass a string representation of a float into int, or a string representation of anything but an integer (including empty string)

#print(compute_total_price({"keyboard": 25.5, "mouse": 10.6}, [("keyboard", 1), ("mouse", 3)]))
#print(compute_total_price({"A": 2.5, "B": 4.0, "C": 9.0}, [("A", 2), ("C", 10)]))
#print(compute_total_price({"a": 1.0, "b": 2.0, "c": 3.0}, [("a", 0), ("b", 1), ("c", 2), ("b", 2)]))
#print(compute_total_price({"a": 1.0, "b": 2.0}, [("b", 1), ("c", 2)]))
print(compute_total_price({"a": 1.0, "b": 2.0}, []))