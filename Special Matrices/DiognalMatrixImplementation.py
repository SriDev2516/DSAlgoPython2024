# BackGround
"""
Diagonal Matrix is a matrix where all elements are zero expect the diagonal elements
Here we will represent a diagonal matrix with help of single dimensional array
Why?
To save space. It will be meaningless to create all elements of a diagonal matrix.
Because most of the elements will be zero.
"""


class DiagonalMatrix:
    def __init__(self, size):
        self.A = [0] * (size+1)


class DiagonalMatrixImplementation:
    def __init__(self, value):
        self.obj = DiagonalMatrix(value)

    def set(self, i, j, value):
        if i == j:
            self.obj.A[i] = value

    def get(self, i, j):
        if i == j:
            return self.obj.A[i]
        else:
            return 0

    def display(self):
        i = 0
        arr_size = len(self.obj.A)

        while i < arr_size:
            j = 0
            while j < arr_size:
                if i == j:
                    print(self.obj.A[i], end=", ")
                else:
                    print(0, end=", ") if j < arr_size else print("puli")
                j += 1
            print()
            i += 1


diagonalImplementation = DiagonalMatrixImplementation(5)
diagonalImplementation.set(0, 0, 5)
diagonalImplementation.set(1, 1, 5)
diagonalImplementation.set(2, 2, 3)
diagonalImplementation.set(3, 3, 1)
diagonalImplementation.set(4, 4, 9)
diagonalImplementation.set(5, 5, 10)

diagonalImplementation.display()
