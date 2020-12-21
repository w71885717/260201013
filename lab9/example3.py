
def get_numbers_of_even(my_list):
    if len(my_list) == 0:
        return 0
    counter = 0
    if my_list[0] % 2 == 0:
        counter = 1
    return counter + get_numbers_of_even(my_list[1:])

print(get_numbers_of_even([0,1,2,3,4,5,6]))