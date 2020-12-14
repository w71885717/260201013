def is_prime(n):
  if n < 2:
    return False
  for i in range(2,n):
    if (n % i) == 0:
      return False
    else:
      continue
  return True
def print_primes_between(b,e):
  for i in range(b,e):
    if is_prime(i):
      print(i, end=" ")
def main():
    x = int(input("Enter first number:"))
    y = int(input("Enter second num:"))
    print_primes_between(x, y)
print(main())




  