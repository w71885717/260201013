students=int(input("how many student:"))
liste=[]
for i in range(students):
  exam1=int(input("Exam1:"))
  exam2=int(input("Exam2:"))
  exam3=int(input("Exam3:"))
  avarege=exam1*(30/100)+exam2*(30/100)+exam3*(40/100)
  liste.append(avarege)
for i in liste:
  print("student",i)
  
