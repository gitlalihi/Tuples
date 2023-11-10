#Python – Remove Tuples from having every element as None
userinput= input("Enter your elements:").split(',')
userlist=[int(i)for i in userinput]
usertuple=tuple(userlist)
print("Your tuple is :",usertuple)
res = [i for i in usertuple if not all(ele == None for ele in i)]
print("Your tuple after removing none",res)