names=[]
sallaries=[]
employees={}
for i in range(5):
  name=input("what's the name:")
  sallary=input("What's the sallary:")
  names.append(name)
  sallaries.append(sallary)
for i in range(len(sallaries)):
  employees[names[i]]=sallaries[i]
print(employees)