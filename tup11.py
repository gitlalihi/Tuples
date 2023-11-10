#Python – All pair combinations of 2 tuples
userinput= input("Enter your elements:").split(',')
userlist=[int(i)for i in userinput]
usertuple=tuple(userlist)
print("Your tuple is :",usertuple)

userinput1= input("Enter your elements:").split(',')
userlist1=[int(i)for i in userinput1]
usertuple1=tuple(userlist1)
print("Your 2nd tuple is :",usertuple1)

result=[(x,y)for x in usertuple for y in usertuple1]
result=result+[(x,y) for x in usertuple1 for y in usertuple]
print("Your all pair combinations is :",result)