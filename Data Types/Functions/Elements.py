"""
https://www.cuemath.com/algebra/types-of-functions/

Based on Elements:
Let A,B bet sets. Let f:A->B. We can consider the set of all possible functions f as the union of:
    (1) One to One Functions,
    (2) Many to One Functions,
    (3) Onto Function,
    (4) One to One and Onto,
    (5) Into Function
    (6) Constant Function
"""

class func_elements:
    def __init__(self,A: list, B: list, fun)->None:
        self.domain = A
        self.codomain = B
        self.f = fun

        self.One21 = 0
        self.Many_to_One = 0
        self.Onto = 0
        self.Constant = 0

        self.range =self.calc_range()


    def implication(self):
        if self.One_to_One:

    def implication_Onto(self):
        if self.Onto:
            self.range == self.codomain
        else:
            self.range != self.codomain and set(self.codomain) - set(self.range) != []

    def implication_One21(self):
        if self.One21:
            #random x,y
            len(self.domain) == len(self.range)

    def implication_Constant(self):
        if self.Constant:
            len(self.range) == 1
        else:
            len(self.range) >= len(self.codomain)

    def calc_range(self):
        range = []
        for element in self.domain:
            range.append("f(" + str(element) + ")")
        return range


    
"""
    def compute_range(self):
        range = []
        for element in self.domain:
            range.append(self.f(element))
"""
