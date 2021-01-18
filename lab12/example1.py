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
mylist = [22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25]
Selection_Sort(mylist)
print(mylist)