#Python – Modulo of tuple elements
user_input1 = input("Enter your elements separated by a comma for the 1st tuple: ").split(',')
user_tuple1 = tuple(int(i) for i in user_input1)


user_input2 = input("Enter your elements separated by a comma for the 2nd tuple: ").split(',')
user_tuple2 = tuple(int(i) for i in user_input2)

if len(user_tuple1) != len(user_tuple2):
    print("Error: The two tuples must have the same number of elements.")
else:
    res = []  
    for i in range(len(user_tuple1)):
        element1 = user_tuple1[i]
        element2 = user_tuple2[i]
        remainder =element1 % element2
        res.append(remainder)
    
    res = tuple(res)
    print("The modulus tuple is:", res)

