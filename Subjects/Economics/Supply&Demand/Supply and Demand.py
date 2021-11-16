from Demand import Demand
import sympy as sym
from sympy import symbols
from Supply import Supply
import numpy as np
from Demand import demandFunctions as df

# x axis values
quantity = [x for x in range(0, 11)]

# corresponding y axis values
quantity_copied = quantity.copy()
supply = quantity_copied[::-1]
demand = quantity


class S_and_D:

    def __init__(self, inpt_demand=Demand([quantity]), inpt_Supply=Supply([quantity]))->None:

        self.demand_functions = [inpt_demand]
        self.supply_functions = [inpt_Supply]
        self.equilibrium_points = []

        #self.type = self.get_type()
    def find_equilibrium(self):
        for d in self.demand_functions:
            for s in self.supply_functions:
                for x in range(0,len(quantity)):
                    if d.demand_vals[x] == s.supply_vals[x]:
                        return [x,d.demand_vals[x]]
                #self.equilibrium_points.append(quantity[idx],d[idx])

    #def get_type(self)->df:
        #if self.demand.type == 1 == self.supply.type:
        #    return df(1)
        #return df(2)

    def solve(self):


    """
    def get_eq(self):
        if
        def graph(self):
    """


a = S_and_D()
print(a.demand_functions[0].demand_vals,a.supply_functions)
print(a.find_equilibrium())