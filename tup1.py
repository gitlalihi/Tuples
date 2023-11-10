#Find the size of a Tuple in Python
userinput=input("Enter your elements seperated by a comma:").split(',')
try:
    usertuple=tuple(userinput)
    size=len(usertuple)
    print("Your tuple:", usertuple)
    print("Size of the tuple is:", size)
except ValueError:
    print("Invalid input. Please enter elements separated by commas.")