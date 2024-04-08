
# Description:
"""
This problem solves addition to two sparse matrices

Sparce Matrix:
    Any matrix which contains more numbers of zeros is known as sparse matrix.

Idea behind:
    We will be representing a sparse matrix in a 3 column representation
    This will minimize the space

3-Col- Rep
    here we will save the row, column and non-zero value of a matrix

Once we create the 3-Col Rep of the matrices, it will be easy to add, substract and multiply

"""

# Algorithm:
"""
1. Create the 3-col rep of Matrix1 and 2
2. The result will be a 3-Col Rep of the addition of two matrices
3. iterate over the matrix1 and matrix2 like below
    a. if matrixa.row < matrixb.row => add matrixa.element
    b. elif: matrixa.row > matrixb.row => add matrixb.element
    c. else: 
        d. if matrixa.col < matrixb.col => add matrixa.element
        e. elif matrixa.col > matrixb.col => add matrixb.element
        f. else: add element.value = matrixa.value+matrixb.value (here both the row and col are same)
"""

class Element:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.value = 0


class SparseMatrix:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.non_zero_elements = 0
        self.elements = []


def create_matrix(matrix):
    sparse_matrix = SparseMatrix()
    sparse_matrix.m = len(matrix)
    sparse_matrix.n = len(matrix[0])
    i = 0
    while i < sparse_matrix.m:
        j = 0
        while j < sparse_matrix.n:
            if matrix[i][j] != 0:
                element = Element()
                element.row = i
                element.col = j
                element.value = matrix[i][j]
                sparse_matrix.elements.append(element)
            j += 1
        i += 1
    sparse_matrix.non_zero_elements = len(sparse_matrix.elements)
    return sparse_matrix


def display_matrix(mat: SparseMatrix):
    i = 0
    k = 0
    while i < mat.m:
        j = 0
        while j < mat.n:
            if k < mat.non_zero_elements and (mat.elements[k].row == i and mat.elements[k].col == j):
                print(mat.elements[k].value, end=", ")
                k += 1
            else:
                print(0, end=", ")
            j += 1
        i += 1
        print()


mata = [
    [1, 2, 3],
    [0, 0, 0],
    [0, 1, 0]
]

matb = [
    [1, 2, 3],
    [0, 0, 0],
    [0, 1, 0]
]

smat_a = create_matrix(mata)
display_matrix(smat_a)

print("************************************")

smat_b = create_matrix(matb)
display_matrix(smat_b)

print("************************************")


def add(input1, input2):
    i = 0
    k = 0
    j = 0

    sparse_matrix = SparseMatrix()
    sparse_matrix.m = input1.m
    sparse_matrix.n = input1.n
    sparse_matrix.elements = []

    while i < input1.non_zero_elements and j < input2.non_zero_elements:
        if input1.elements[i].row < input2.elements[j].row:
            sparse_matrix.elements.append(input1.elements[i])
            i += 1
        elif input1.elements[i].row > input2.elements[j].row:
            sparse_matrix.elements.append(input2.elements[j])
            j += 1
        else:
            if input1.elements[i].col < input2.elements[j].col:
                sparse_matrix.elements.append(input1.elements[i])
                i += 1
            elif input1.elements[i].col > input2.elements[j].col:
                sparse_matrix.elements.append(input2.elements[j])
                j += 1
            else:
                element = Element()
                element.row = input1.elements[i].row
                element.col = input1.elements[i].col
                element.value = input1.elements[i].value + input2.elements[j].value
                sparse_matrix.elements.append(element)
                j += 1
                i += 1

    while i < input1.non_zero_elements:
        sparse_matrix.elements.append(input1.elements[i])
        i += 1

    while j < input2.non_zero_elements:
        sparse_matrix.elements.append((input2.elements[j]))
        j += 1

    sparse_matrix.non_zero_elements = len(sparse_matrix.elements)
    return sparse_matrix


result = add(smat_a, smat_b)
display_matrix(result)