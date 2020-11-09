x=input("write a num:")
list=[]
for i in x:
  list.append(i)
list.reverse()
ans=int(list[0])+int(list[1])
print(ans)