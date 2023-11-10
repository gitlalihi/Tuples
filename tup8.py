#Python | Update each element in tuple list
def update_tuples(tuples_list, new_val):
    for i in range(len(tuples_list)):
        x, y, z = tuples_list[i]
        tuples_list[i] = (new_val, y, z)
    return tuples_list
tuple_list = []
for i in range(4):  
    element1 = input("Enter the first element: ")
    element2 = input("Enter the second element: ")
    element3= input("Enter the third element: ")
    tuple_list.append((element1, element2,element3))
print(tuple_list)
new_val = input("Enter your number:")
updated_tuples = update_tuples(tuple_list, new_val)
print(updated_tuples)