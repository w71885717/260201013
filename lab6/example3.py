students=int(input("how many student:"))
liste=[]
for i in range(students):
  exam1=int(input("Exam1:"))
  exam2=int(input("Exam2:"))
  exam3=int(input("Exam3:"))
  avarege=exam1*(30/100)+exam2*(30/100)+exam3*(40/100)
  liste.append(avarege)
avarege_grades_greater_than_90 = []
for i in liste:
  if i > 90:
    avarege_grades_greater_than_90.append(i)
print(avarege_grades_greater_than_90)