#Python program to sort a list of tuples by second Item
tlist=int(input("Enter the number of your Tuples in list:"))
tup_list=[]
for i in range(tlist):
    ele1=input(f"Enter your 1st element{i+1} :")
    ele2=input(f"Enter your 2nd elemnent{i+1} :")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your tuple list is :",tup_list)

def get_first_element(t):
    return t[0]

sorted_tuple=sorted(tup_list,key=get_first_element)
print("Your sorted tuples is :",sorted_tuple) 