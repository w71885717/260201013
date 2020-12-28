def sum_list(x):
  if not isinstance(x, list):
    return x
  else:
    sum_result = 0
    for item in x:
      sum_result += sum_list(item)
    return sum_result
print(sum_list([3,12,76,[4,56,43],[2,8],81,75]))