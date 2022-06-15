def compute_product(list_of_integers):
    """returns the product of the odd integers in the list, If the list doesn’t contain any odd integer, the function returns 1."""
    final_product = 1
    for number in list_of_integers:
        if number % 2 == 1:            # if remainder is 1, odd number
            final_product *= number
    return final_product

#print(compute_product([1, 2, 3, 4]))
#print(compute_product([1, 3, 5]))
#print(compute_product([2, 4, 6, 8, 111]))
#print(compute_product([-2, -3, -5, -3, 100]))
#print(compute_product([4, 40, 400]))
#print(compute_product([]))