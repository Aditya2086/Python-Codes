# 4. To write a Python Program to find the maximum from a list of numbers.

n=int(input("Enter number of element in list"))
mylist=[]
print("Enter elements of the list")
for _ in range(n):
    a=int(input())
    mylist.append(a)
maximum=max(mylist)
print("Maximum of the list is :",maximum)
