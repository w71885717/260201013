import random
random.seed(123)

def get_random_list(b, e, N):
  #random list
  r_list = random.sample(range(b, e), N)
  return r_list


def get_overlap(L1, L2):
  L3 = []
  for num in L1:
    if num in L2:
      L3.append(num)
  return L3

def main():
  list_1 = get_random_list(b=0, e=10, N=5)
  list_2 = get_random_list(b=0, e=10, N=5)
  print(list_1)
  print(list_2)
  list_3 = get_overlap(list_1,list_2)
  print(list_3)
main()