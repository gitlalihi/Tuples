#Python | Multiply Adjacent elements

user_input1 = input("Enter your elements separated by a comma for the 1st tuple: ").split(',')
user_tuple1 = tuple(int(i) for i in user_input1)
print("Your tuple is:", user_tuple1)

# Multiply adjacent elements
result =tuple(user_tuple1[i] * user_tuple1[i+1] for i in range(len(user_tuple1) - 1))
print("Your product after multiplying adjacent elements is:", result)