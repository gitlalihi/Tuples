#Python – Sort Tuples by Total digits
tlist=int(input("Enter the number of your Tuples in list:"))
tup_list=[]
for i in range(tlist):
    ele1=input(f"Enter your 1st element{i+1} :")
    ele2=input(f"Enter your 2nd elemnent{i+1} :")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your tuple list is :",tup_list)

def total_digits(t):
    return sum([len(str(ele))for ele in t])

sorted_tuple=sorted(tup_list,key=total_digits)
print("Your sorted tuples by total digits :",sorted_tuple) 