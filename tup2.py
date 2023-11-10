#Python – Maximum and Minimum K elements in Tuple
userinput=input("Enter your elements seperated by a comma:").split(",")
usertuple=tuple(userinput)
print("Your tuple:", usertuple)
k= 2
testtuple= list(usertuple)
temp=sorted(testtuple)
result=tuple(temp[:k]+temp[-k:])
print("Your maximum and minimum k elements in tuple is:",result)
