my_list = [1,2,3,4]
def reverse_list(my_list):
    if len(my_list) == 0:
        return []
    else:
        return [my_list.pop()] + reverse_list(my_list)
print(reverse_list(my_list))