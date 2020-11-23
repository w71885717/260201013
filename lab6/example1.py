email = input("Please enter an email address:")
new_mail = "ceng113@example.com"
if "@" in email: 
  email = email.lower()
  part_1 = email.split("@")[0]
  part_1 = part_1.replace(".", "")
  part_2 = email.split("@")[1]
  email = part_1 + "@" + part_2
  print(email)
  if email == new_mail:

    print("True")
  else:
    print("False")
else:
  print("False")