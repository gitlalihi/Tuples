#Python program to create a list of tuples from given list having number and its cube in each tuple
list=input("Enter your elements:").split(',')
result=[(int(ele) ,pow (int(ele),3)) for ele in list ]
print("Your cube of numbers with a list of tuples is :",result)