matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
groceries = [["apple", "banana"], ["bread", "milk"], ["cheese"]]
print(groceries)
first_row = matrix[0]
print(first_row)
middle_item = groceries[1][0]
print(middle_item)
matrix[1][2] = 10
groceries[0].append("orange")
for row in matrix:
    for item in row:
        print(item)



