from vector import vector
from typing import List
import sympy as sym
from sympy import symbols, functions

"""
(1) Operator Overloading, and use of vector sum


"""


class Matrix:

    def __init__(self, cols: List[vector]):
        self.num_rows = len(cols)
        self.num_cols = len(cols[0])
        self.mat = self.generateMatrix(cols)

    def generateMatrix(self, cols: List[list]) -> List[List[symbols]]:
        new_mat = []
        for col in cols:
            new_mat.append(vector(col))
        return new_mat

    def print_rows(self) -> None:
        for row in self.mat:
            s = row.print_vector()
            print(s + "\n")

    def can_add(self, other):
        if self.num_rows == other.num_rows and self.num_cols == other.num_cols:
            return True
        return False

    def can_mult(self, other):
        if self.num_rows == other.num_cols:
            return True
        return False

    def get_row(self, row_num: int) -> vector:
        return self.mat[row_num]

    def add_matrices(self, other):
        if self.can_add(other):
            sum_mat_rows = []
            for x in range(0, self.num_rows):
                other.mat[x]
                row_c = self.mat[x].add_vec(other.mat[x])
                sum_mat_rows.append(row_c)
            return Matrix(sum_mat_rows)

    def get_row(self, row_num: int) -> vector:
        return self.mat[row_num]

    def multiply_matrices(self, other):
        if self.can_mult(other):
            mult_mat_rows = []
            for x in range(0, self.num_rows):
                mat_row = []
                for y in range(0, other.num_cols):
                    mat_row.append(self.mat[x].dot_product(other.mat[y]))
                mult_mat_rows.append(mat_row)

            return Matrix(mult_mat_rows)

    def is_square(self):
        return self.num_rows == self.num_cols

    def determinant(self) -> float:
        if self.is_square():
            self.compute_determinant()

    """
    Need to do two ways. for now we will do the simple way. eventually will have it scale
    """

    def scale(self, scalar: symbols):
        matt = []
        for row in self.mat:
            row.scale_vec(scalar).print_vector()


'''
    def compute_determinant(self)->float:
        if self.num_rows == 2:
            return self.mat[0][0] * self.mat[1][1] - self.mat[0][1] * self.mat[1][0]
        else:
            return
    def deleted_matrix(self, row_num: int, col_num: int):
'''

'''
    #def print_cols(self):


a= Matrix([[1, 2, 3], [4, 5, 6]])
b= Matrix([[2,3,4],[3,4,5]])
print(a.get_row(1))

c = a.add_matrices(b)
c.print_rows()
'''
a = Matrix([[2, 0], [0, 2]])

b = symbols("b")
c = a.scale(b)
