#Python – Records with Value at K index
t=int(input("Enter your number of tuples:"))
tup_list=[]
for i in range (t):
    ele1=input(f"Enter your 1 st element {i+1} :")
    ele2=input(f"Enter your 2nd element {i+1} :")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your tuple list is :",tup_list)
k=input("Enter your index you want to search the element at:")
result_list=[]
for tup in range(t):
    if tup== k:
        result_list.append(tup)
print(f"Your elements at the k th index is :",result_list)
