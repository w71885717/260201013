N=int(input("How many numbers:"))
liste=[]
a=0
for i in range (N):
  x=int(input("Number:"))
  liste.append(x)
for i in liste:
  if i%2==0:
    a=a+1
print(a/N)

