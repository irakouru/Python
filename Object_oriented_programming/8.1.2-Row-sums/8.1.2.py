"""Please write a function named row_sums(my_matrix: list), which takes an integer matrix as its argument.

The function should add a new element on each row in the matrix. This element contains the sum of the other 
elements on that row. The function does not have a return value. It should modify the parameter matrix in place."""

def row_sums(my_matrix: list):
    for item in my_matrix:
        row_sum = 0
        for value in item:
            row_sum += value
        item.append(row_sum)

my_matrix = [[1, 2, 6], [3, 4, 10], [6, 3, 7], [0, 0], [1, 1, 1, 1, 1]]
row_sums(my_matrix)
print(my_matrix)