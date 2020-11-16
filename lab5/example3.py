num1=int(input("number 1:"))
num2=int(input("number 2:"))
match=0

while num1>0 and num2>0:
  if num1%10==num2%10:
    match+=1
    num1 = num1 // 10
    num2 = num2 // 10
print("Match:", match)