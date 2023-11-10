#Python – Adding Tuple to List and vice – versa
userinput=input("Enter your elements seperated by a comma:").split(",")
print(" Your list is :",userinput)

userinput1=input("Enter your elements seperated by a comma:").split(',')
usertuple=tuple(userinput1)
print("Your tuple is :" , usertuple)

result=tuple(userinput+list(usertuple))
print(" Adding Tuple to list and vice-versa:",result)