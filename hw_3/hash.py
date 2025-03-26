import numpy as np
from functools import lru_cache

class HashMix:
    @lru_cache(maxsize=None)
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

    def __eq__(a, b):
        if a.rows != b.rows or a.cols != b.cols:
            return False
        rows = a.rows
        cols = b.cols
        for i in range(rows):
            for j in range(cols):
                if a.matrix[i][j] != b.matrix[i][j]:
                    return False
        return True

    def __hash__(self):
        """
        Функция:
        1. Считается сумма всех элементов матрицы
        2. Результатом является остаток суммы от количества элементов
        """

        s = 0

        for i in range(self.rows):
            for j in range(self.cols):
                s += self.matrix[i][j]
        return s % (self.rows * self.cols)
    

class Matrix(HashMix):
    def __init__(self, m):
        self.matrix = m
        self.rows = len(m)
        self.cols = len(m[0])
            

def Collision():
    np.random.seed(0)
    while True:
        arr1 = np.random.randint(0, 10, (10, 10)).tolist()
        arr2 = np.random.randint(0, 10, (10, 10)).tolist()
        A = Matrix(arr1)
        C = Matrix(arr2)
        if hash(A) == hash(C) and A != C:
            arr = np.random.randint(0, 10, (10, 10)).tolist()
            B = Matrix(arr)
            D = B
            AB = A @ B
            CD = C @ D
            if AB != CD:
                return A, B, C, D, AB, CD
            


A, B, C, D, AB, CD = Collision()

with open("A.txt", "w") as file:
    file.write(str(A.matrix) + "\n")

with open("B.txt", "w") as file:
    file.write(str(B.matrix) + "\n")

with open("C.txt", "w") as file:
    file.write(str(C.matrix) + "\n")

with open("D.txt", "w") as file:
    file.write(str(D.matrix) + "\n")

with open("AB.txt", "w") as file:
    file.write(str(AB.matrix) + "\n")

with open("CD.txt", "w") as file:
    file.write(str(CD.matrix) + "\n")

with open("hash.txt", "w") as file:
    file.write("AB: " + str(hash(AB)) + "\n")
    file.write("CD: " + str(hash(CD)) + "\n")
