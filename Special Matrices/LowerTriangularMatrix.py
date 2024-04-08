# Description

"""
Lower triangular matrix is defined as follows:
M[i, j] = 0,  i < j
M[i, j] != 0, i >= j

So there is a formula to know the index of the element in a linear array

Index of M[i, j] =  i * (i+1) / 2 + j

Size of the Linear array = n*(n+1)/2, where n is the size of the matrix
"""


class Matrix:
    def __init__(self, n):
        self.A = [0] * n


class TriangularMatrixImplementation:
    def __init__(self, n):
        self.arr_size = n * (n + 1) // 2
        self.obj = Matrix(self.arr_size)
        self.matrix_len = n

    def set(self, roe, col, value):
        if roe >= col:
            self.obj.A[(roe * (roe + 1) // 2) + col] = value

    def display(self):
        row = 0
        while row < self.matrix_len:
            col = 0
            while col < self.matrix_len:
                if row >= col:
                    print(self.obj.A[(row * (row + 1) // 2) + col], end=', ')
                else:
                    print(0, end=", ")
                col += 1
            print()
            row += 1


customer_input = 56
lower_triangle = TriangularMatrixImplementation(customer_input)

i = 0
while i < customer_input:
    j = 0
    while j < customer_input:
        if i >= j:
            lower_triangle.set(i, j, 1)
        j += 1
    i += 1

lower_triangle.display()
