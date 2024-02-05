"""Write an algorithm (using pseudocode or any known programming language) for the following computational tasks:
1)	Given a matrix, print the element at (0,0).
2)	Given a matrix, double all elements of its first row.
3)	Given a matrix, double all elements of the entire matrix.
Analyze the (theoretical) time complexity of these three algorithms. If you wish, you can also test the empirical time 
complexity using the same method as shown during lectures (using Python libraries pandas, numpy and matplotlib).
"""
# 1)

def print_first_element(matrix: list):
    return matrix[0][0]

# 2)

def double_first_row(matrix: list):
    first_row = matrix[0]
    for index in range(0, len(first_row)):
        first_row[index] = first_row[index] * 2

    return matrix

# 3)

def double_all_the_elements(matrix: list):
    for i in range(0, len(matrix)):
        for j in range(0,len(matrix[i])):
            matrix[i][j] = matrix[i][j] * 2

    return matrix


"""def copy_first_row(matrix: list):
    insert_list = [matrix[0]]
    pos = 1
    matrix[pos:pos] = insert_list
    print(matrix)"""

print(print_first_element([[1, 2, 3, 4], [7, 9, 5, 4]]))
#copy_first_row([[1, 2, 3, 4], [7, 9, 5, 4]])
print(double_first_row([[1, 2, 3, 4], [7, 9, 5, 4]]))
print(double_all_the_elements([[1, 2, 3, 4], [7, 9, 5, 4]]))

