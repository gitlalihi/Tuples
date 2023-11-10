#Python | Test if tuple is distinct
userinput=input("Enter your elements seperated by a comma:").split(',')
userlist=[int(i)for i in userinput]
usertuple=tuple(userlist)
result=set()
flag=True
for i in usertuple:
    if i in result:
        flag=False
        break
    result.add(i)
print("Is tuple distinct? :",flag)    