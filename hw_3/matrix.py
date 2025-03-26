import numpy as np

class Matrix:
    def __init__(self, m):
        self.matrix = m
        self.rows = len(m)
        self.cols = len(m[0])
        
    def __add__(a, b):
        if a.rows != b.rows or a.cols != b.cols:
            raise ValueError("Wrong size")
        
        rows = a.rows
        cols = a.cols
        
        res = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = a.matrix[i][j] + b.matrix[i][j]
        return Matrix(res)

    def __mul__(a, b):
        if a.rows != b.rows or a.cols != b.cols:
            raise ValueError("Wrong size")
        
        rows = a.rows
        cols = a.cols
        
        res = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = a.matrix[i][j] * b.matrix[i][j]
        return Matrix(res)

    def __matmul__(a, b):
        if a.cols != b.rows:
            raise ValueError("Wrong size")
        
        rows = a.rows
        cols = b.cols
        
        res = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for k in range(cols):
                    res[i][j] += a.matrix[i][k] * b.matrix[k][j]
        return Matrix(res)
    

np.random.seed(0)
arr1 = np.random.randint(0, 10, (10, 10)).tolist()
arr2 = np.random.randint(0, 10, (10, 10)).tolist()

matrix1 = Matrix(arr1)
matrix2 = Matrix(arr2)

add_result = matrix1 + matrix2
mul_result = matrix1 * matrix2
matmul_result = matrix1 @ matrix2

with open("matrix+.txt", "w") as file:
    file.write("matrix1:\n" + str(matrix1.matrix) + "\n")
    file.write("matrix2:\n" + str(matrix2.matrix) + "\n")
    file.write("result:\n" + str(add_result.matrix) + "\n")

with open("matrix∗.txt", "w") as file:
    file.write("matrix1:\n" + str(matrix1.matrix) + "\n")
    file.write("matrix2:\n" + str(matrix2.matrix) + "\n")
    file.write("result:\n" + str(mul_result.matrix) + "\n")

with open("matrix@.txt", "w") as file:
    file.write("matrix1:\n" + str(matrix1.matrix) + "\n")
    file.write("matrix2:\n" + str(matrix2.matrix) + "\n")
    file.write("result:\n" + str(matmul_result.matrix) + "\n")

