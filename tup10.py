#Python – Join Tuples if similar initial element
userinput=input("Enter your elements seperated by a comma:").split(',')
userlist=[int(i)for i in userinput]
usertuple=tuple(userlist)

result = []

for i in usertuple:
    if result and tuple(result[-1])[0] == i:
        result[-1] =result[-1] + (i,)
    else:
        result.append((i,))

print("The extracted elements: " + str(result))