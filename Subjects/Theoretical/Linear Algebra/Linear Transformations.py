import mpmath

import matrix
from matrix import Matrix

"""
Modificiations: 

(1) constructor ; default 
    (a) First 2 parameters need to change to a vector space
    (b) How do we call in a function as a parameter itself
    
(2) Evenetually need to consider Fields 
(3) line 111 - better method for doing this
"""

"""
Planning-Ideas:
https://www.google.com/url?sa=i&url=https%3A%2F%2Fmath.stackexchange.com%2Fquestions%2F3512209%2Fcartesian-coordinates-and-linear-transformation&psig=AOvVaw392Q894AOmYxNo_ZYT_1bb&ust=1636908140118000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCND1vJPklfQCFQAAAAAdAAAAABAD
(1) We should write T as a matrix!!!
    (a)Use Matrix Class
    (b) Method of conversion 
        - Input T as a list of transformations for that particular dimension 
            -- T(a,b) = (3a + 4b, 1a - 2b, 4a)
                *len of T(a,b) = number of rows in matrix 
                *len of (a,b) = number of columns in matrix 
        - Output as Matrix
            -- T = [ [3,4] ,
                     [1,2] , 
                     [4,0] ]    
         

(2)
"""


# https://www.geeksforgeeks.org/split-string-substrings-using-delimiter/
def splitStrings(st, dl):
    word = ""

    # to count the number of split strings
    num = 0

    # adding delimiter character at
    # the end of 'str'
    st += dl

    # length of 'str'
    l = len(st)

    # traversing 'str' from left to right
    substr_list = []
    for i in range(l):

        # if str[i] is not equal to the
        # delimiter character then accumulate
        # it to 'word'
        if (st[i] != dl):
            word += st[i]

        else:

            # if 'word' is not an empty string,
            # then add this 'word' to the array
            # 'substr_list[]'
            if (len(word) != 0):
                substr_list.append(word)

            # reset 'word'
            word = ""

    # return the splitted strings
    return substr_list


a = ["3v_{1} + 4v_{2}", "1v_{1}  + -1v_{2}", "4v_{1}"]


class linearTransformation:

    def __init__(self, domain: set, codomain: set, function_def: list) -> None:
        self.domain = domain
        self.codomain = codomain
        self.linearTrans = function_def

    '''

    def LHS_computation(self):
        return T(c*x + y)

    def RHS_computation(self):
        return c * T(x) + T(y)
    '''

    def is_linear(self):
        return self.LHS_computation() == self.RHS_computation()

    def T(self):
        num_cols = self.domain.dim
        num_rows = self.codomain.dim

    def convert_T(self, linear_T: list):
        T_mat = []

        for item in linear_T:
            item.strip.replace(" ", "")
            row_comps = splitStrings(item, "+")
            return row_comps
            row_vec = [0] * len(self.linearTrans)
            for row in row_comps:
                basis_index = row.find("v")
                v_index_lowerLimit = row.find("{")
                v_index_upperLimit = row.find("}")
                v_index = row[v_index_lowerLimit:v_index_upperLimit]
                scalar = row[:basis_index]
                row_vec[v_index] = scalar
            T_mat.append(row_vec)
        return Matrix(T_mat)


def convert_T(linear_T: list):
    T_mat = []

    for item in linear_T:
        item.replace(" ", "")
        row_comps = splitStrings(item, "+")
        row_vec = [0] * (len(linear_T)-1)
        for row in row_comps:

            basis_index = row.find("v")
            v_index_lowerLimit = row.find("{")
            v_index_upperLimit = row.find("}")
            v_index = row[v_index_lowerLimit+1:v_index_upperLimit]
            scalar = int(row[: basis_index])
            row_vec[int(v_index)-1] = scalar
        #print(row_vec)
            #row_vec[v_index]
        T_mat.append(row_vec)
    return Matrix(T_mat)

"""
LHS: cT(x) + T(y)
"""
def compute_LHS:
    c = symbols("c")
    T_x = T.multiply_matrices(Matrix([x]))
    T_y = T.multiply_matrices(Matrix([y]))
    cT_x = T_x.scale(c)
    expr = cT_x + T_y
    return expr
"""
RHS: T(cx + y)
*DOOOOOOOOOOOOOOOOOOOOOO
"""
def compute_LHS:
    c = symbols("c")
    cx = x.scale_vec(c)
    cxpy = cx + y
    T_cxpy = T.multiply_matrices(Matrix([cxpy]))
    expr = cT_x + T_y
    return expr

def is_linearTrans(self)->bool:
    return self.compute_LHS == self.compute_RHS








C = convert_T(a)
C.print_rows()