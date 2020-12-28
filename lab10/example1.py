def multiple(n):
  if n == 1:
    return 3
  else:
    return 3 + multiple(n-1)





print(multiple(5))