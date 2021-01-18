def Selection_Sort(mylist): 
    for i in range(len(mylist)):
        min_1 = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[min_1]:
                min_1 = j 
        temp = mylist[i]
        mylist[i] = mylist[min_1]
        mylist[min_1] = temp
    return mylist 


def binary_search(our_list, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if our_list[mid] == x: 
            return mid 
        elif our_list[mid] > x: 
            return binary_search(our_list, low, mid - 1, x) 
        else: 
            return binary_search(our_list, mid + 1, high, x) 
    else: 
        return -1

my_list = [22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25]
my_list = Selection_Sort(my_list)
element = 8

result = binary_search(my_list, 0, len(my_list)-1, element) 
  
if result != -1: 
    print("Element at index:", str(result)) 
else: 
    print("Element is not in list") 