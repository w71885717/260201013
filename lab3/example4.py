age=int(input("what's your age:"))
if age<6 or age>60:
  ticket=0
elif age>6 and age<18:
  ticket=3/2
else:
  ticket=3
print(ticket)