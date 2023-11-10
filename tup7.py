#Python – Row-wise element Addition in Tuple Matrix
matrix = []
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
for i in range(num_rows):
   
    row = []
    for j in range(num_cols):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
matrix.append(tuple(row))
print("Input Matrix:")
for r in matrix:
    print(r)

row_sums = []

for row in matrix:
   row_sum = sum(row)
   row_sums.append(row_sum)

for i, row_sum in enumerate(row_sums):
    print(f"Row {i + 1} sum: {row_sum}")
