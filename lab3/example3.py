gpa=float(input("Your gpa:"))
lec=float(input("Your lecture number:"))
if gpa<2:
  if lec<47:
    print("not enough number of lectures and gpa")
  else:
    print("not enough gpa")
else:
  if lec<47:
    print("not enough number of lectures")
  else:
    print("graduated!")