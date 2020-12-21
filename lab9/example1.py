def recursive_func(n):
  if n == 0:
    return n
  else:
    return (1/n) + recursive_func(n-1) 
print(recursive_func(5))