from typing import List
import sympy
from sympy import symbols,functions

"""
Univariate
Need to generalize to functions
"""

c = symbols("c")

class model_functions:

    def __init__(self, t_domain=[x for x in range(0, 11)]) -> None:
        """

        :param type: d or i(direct or indirect)
        :param t_domain:
        """
        self.domain = self.codomain = t_domain
        # self.type = type


        # def set_codomain(self)->list:
        """
        uses model_function type to determine the relationship between codomain and domain.
        :return: codomain
        """
        # if self.type != "d":
        # return self.domain[::-1]
        # return self.domain
    def __init__(self, domain: list, func: functions) -> None:
        """

        :param type: d or i(direct or indirect)
        :param t_domain:
        """
        self.domain = domain
        self.f = func
        self.codomain =
        # self.type = type



class Demand(model_functions):
    def __init__(self, name="D_0", t_domain=[x for x in range(0, 11)]) -> None:
        super().__init__()
        self.codomain = t_domain[::-1]
        #self.codomain = t_domain
        # self.domain,self.codomain = t_domain
        self.domain_type = "Quantity Demanded"
        self.codomain_type = "Price Demanded"
        self.name = name
    def __init__(self,D_func: functions,name="D_0")->None:
        self.f = D_func
        self.var = self.f.free_symbols[0]
        self.x_upper_bounds = self.get_lowerBounds()[0]
        self.x_lower_boonds = self.f.evalf(subs={c:0})

        self.domain = self.get_domain()
    def get_Bounds(self):
        sympy.solve(self.f,self.f.free_symbols)
    def evaluate_demand(self,val):
        return self.f.evalf(subs={c: val})


class Supply(model_functions):
    def __init__(self, name="S_0", t_domain=[x for x in range(0, 11)]) -> None:
        super().__init__()
        # self.demand,self.price = t_domain
        self.domain_type = "Quantity Supplied"
        self.codomain_type = "Price Supplied"
        self.name = name

class Price(model_functions):
    def __init__(self,p: int, name="P_0", t_domain=[x for x in range(0, 11)]) -> None:
        super().__init__()
        self.codomain = [p] * len(t_domain)
class Quantity(model_functions):
    def __init__(self,q: int, name="P_0", t_domain=[x for x in range(0, 11)]) -> None:
        super().__init__()
        self.domain = [q] * len(t_domain)
        self.codomain = t_domain
    def __init__(self,D_func: functions,name="D_0")->None:
        self.f = D_func
        self.var = self.f.free_symbols[0]
        self.x_upper_bounds = self.get_lowerBounds()[0]
        self.x_lower_boonds = self.f.evalf(subs={c:0})

    def evaluate_supply(self,val):
        return self.f.evalf(subs={c: val})
"""
Test 0: model_functions base testing. 
        (1) Creating and initializing an obect with the empty constructor.(+)
        (2) Checking that the codomain and domain are initialized properly.(+) 
"""
a = model_functions()
print(a.domain,a.codomain)
"""
Test 1: Demand and Supply Base Testing. 
        (1) Creating and initializing an obect with the empty constructor.(-,-)
        (2) Checking that the codomain and domain are initialized properly.(-,-)
        (3) Checking that the domain_type,codomain_type, and the name are initialized properly.(-,-)
        (4)
"""
a1 = Demand()
b1 = Supply()
print(a1.domain,a1.codomain,a1.codomain_type,a1.domain_type,a1.name)
print(b1.domain,b1.codomain,b1.codomain_type,b1.domain_type,b1.name)

