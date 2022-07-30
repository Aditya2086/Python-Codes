# 10. To write a Python program to find first n prime numbers.


# change the values of lower and upper for a different result
lower =  int(input(“Enter number starting: “)) 
upper =  int(input(“Enter number ending: “)) 

print(“Prime numbers between”,lower,”and”,upper,”are:”)

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
