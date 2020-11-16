num1=input("number 1:")
num2=input("number 2:")
list1=[]
for i in num1:
  list1.append(i)
for i in num2:
  if i in list1:
    print(i)