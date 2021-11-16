"""
Ideas:
(1) Construtors:
    (a) explicitly define product of all elements
    (b)
(2) Second Constructor -> we need to ensure that the operation matrix is defined as part of the matrix class
(3)
(4)

"""
from typing import List
import sympy as sym
from sympy import symbols


class Group:

    def __init__(self, input_set, operation) -> None:
        self.gSet = set
        self.g_op = operation

    def __init__(self, input_set, operationMatrix: List[symbols]) -> None:
        """

        :param input_set: Tjhe set for which the group is formed
        :param operationMatrix: Suppose G has n elements. then the operation matrix is the nxn by matrix with the G_ij entry representing g_i * g_j.
        """
        self.gSet = set
        self.g_op = operationMatrix

    def has_identity(self):
        e = G

    def is_Group(self):
        return self.has_identity and self.has_inverse and self.is_associative
        """
        
        :return: True if a group can be formed, and false otherwise 
        """
