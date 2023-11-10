#Python – Remove Tuples in a list  of Length K
tlist=int(input("Enter the number of your Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=input(f"Enter your 1st element{i+1} :")
    ele2=input(f"Enter your 2nd elemnent{i+1} :")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your tuple list is :",tup_list)


k= input("Enter your length")
result= [ele for ele in tup_list if len(ele)!=k]
print("Your extracted tuples are:",result)