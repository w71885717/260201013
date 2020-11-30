books=["Ulysses","Animal FArm","Brave New World","Ender's Game"]
book_dict={}
first=[]
second=[]
total=0
first1=[]
second1=[]

for i in books:
  for k in i:
    if k in first:
      pass
    else:
      second.append(k)
    first.append(k)
  first1.append(len(first))
  second1.append(len(second))
  first.clear()
  second.clear()


for i in range(len(books)):
  book_dict[books[i]]=(first1[i],second1[i])
print(book_dict)
