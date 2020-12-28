def hailstone(x):
  if x == 1:
    return 1
  elif x % 2 == 0:
    return str(x/2) + ","+ str(hailstone(x-1))
  else:
    return str(3*x+1) + "," + str(hailstone(x-1))

n = int(input("Enter:"))
print(n,hailstone(n))
