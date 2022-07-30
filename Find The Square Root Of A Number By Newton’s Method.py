# 2. To write a Python Program to find the square root of a number by Newton’s Method.

def newton_method(number, number_iters = 100):
a = float(number) 
for i in range(number_iters): 
number = 0.5 * (number + a / number) 

return number

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Square root of first number:",newton_method(a))
print("Square root of second number:",newton_method(b))
