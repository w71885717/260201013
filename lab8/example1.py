def sum_of(a_liste):
  sumation = 0
  for i in a_liste:
    sumation += i
  return sumation ** 2
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(sum_of(a_list))