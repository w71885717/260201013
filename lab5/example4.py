pasw= "abc123"
ask=input("pasword:")
while pasw!= ask:
  if ask == "help":
    print("a")
    break
  elif pasw!= ask:
    print("wrong")
    ask=input("pasword:")
if pasw == ask:
  print("Welcome")