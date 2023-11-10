#Python – Elements frequency in Tuple
userinput=input("Enter your elments:")
userlist=[int(e)for e in userinput]
usertuple=tuple(userlist)
result=dict()
x=list(usertuple)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    result[i]=x.count(i)

print("Your tuple frquency element is :",result)            