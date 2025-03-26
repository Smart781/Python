import numpy as np

class NoteMixin:
    def __str__(self):
        res = ""
        for i in range(self.rows):
            for j in range(self.cols):
                res += str(self.matrix[i][j])
                res += " "
            res += "\n"
        return res

    def save(self, name):
        with open(name, "w") as file:
            file.write(str(self))

class OperationsMixin:
    def __add__(a, b):
        return MatrixMixin(a.matrix + b.matrix)
    
    def __sub__(a, b):
        return MatrixMixin(a.matrix - b.matrix)
    
    def __mul__(a, b):
        if a.rows != b.rows or a.cols != b.cols:
            raise ValueError("Wrong size")
        return MatrixMixin(a.matrix * b.matrix)

    def __truediv__(a, b):
        return MatrixMixin(a.matrix / b.matrix)
    
    def __matmul__(a, b):
        if a.cols != b.rows:
            raise ValueError("Wrong size")
        return MatrixMixin(a.matrix @ b.matrix)
    
    def __eq__(a, b):
        return np.array_equal(a.matrix, b.matrix)

    @property
    def shape(self):
        return self.matrix.shape

    @property    
    def T(self):
        return MatrixMixin(self.matrix.T)
    

class MatrixMixin(NoteMixin, OperationsMixin):
    def __init__(self, m):
        self.matrix = m
        self.rows = m.shape[0]
        self.cols = m.shape[1]


np.random.seed(0)
arr1 = np.random.randint(1, 10, (10, 10))
arr2 = np.random.randint(1, 10, (10, 10))

matrix1 = MatrixMixin(arr1)
matrix2 = MatrixMixin(arr2)

m1 = matrix1 + matrix2
m2 = matrix1 - matrix2
m3 = matrix1 * matrix2
m4 = matrix1 / matrix2
m5 = matrix1 @ matrix2
m6 = matrix1.T

matrix1.save("matrix1.txt")
matrix2.save("matrix2.txt")
m1.save("matrix+.txt")
m2.save("matrix-.txt")
m3.save("matrix∗.txt")
m4.save("matrix∕.txt")
m5.save("matrix@.txt")
m6.save("matrixT.txt")
                         
                         
                
