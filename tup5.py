#Python – Sum of tuple elements
userinput=input("Enter your elements seperated by a comma:").split(',')
userlist=[int(i)for i in userinput]
usertuple=tuple(userlist)
result=sum(usertuple)
print("Your summation of elements in the tuple are:",result)    