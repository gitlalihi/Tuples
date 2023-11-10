#Python – Filter Range Length Tuples
t=int(input("Enter your number of tuples:"))
tup_list=[]
for i in range (t):
    ele1=input(f"Enter your 1 st element {i+1} :")
    ele2=input(f"Enter your 2nd element {i+1} :")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your tuple list is :",tup_list)

x= input("Enter your minimum range")
y= input("Enter your mamximum range")
result=[z for z in range (t)if len(z)>=x and len(z) <= y]
print("Your extracted tuple from your mentioned range is :",result)