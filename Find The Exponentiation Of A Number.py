# 3. To write a Python program to find the exponentiation of a number. 

num=int(input("Enter number: "))
exp=int(input("Enter exponential value: "))
result=1
for i in range(1,exp+1):

result=result*num
print("Result is:",result)
