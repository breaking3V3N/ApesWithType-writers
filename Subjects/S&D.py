import sympy as sym

"""
Assuming a function of the price 

"""

p = sym.symbols("p")


class SD:

    def __init__(self, d, s):
        #
        self.demand_func = d
        self.supply_func = s

        # assuming variable is p at moment
        self.variables = self.demand_func.free_symbols

        #
        self.demand_price_zero = self.xDemand_upperBound()
        self.supply_quantity_zero = self.ySupply_upperBound()

        #
        self.equilibrium_price = self.pEquilibrium()
        self.equilibrium_quantity = self.demand_func.evalf(subs={p: self.equilibrium_price})

        self.equilibrium_point = [self.equilibrium_quantity, self.equilibrium_price]

        self.modify_price = 0
        self.modify_quantity = 0

    def set_price(self, price: float) -> None:
        self.modify_price = 1
        self.new_price = price
        self.new_quantityByPrice()

    def set_quantity(self, quantity: float) -> None:
        self.modify_quantity = 1
        self.modified_quantity = quantity

    def new_quantityByPrice(self):
        while self.modify_price:
            new_QD = self.demand_func.evaluate_demand()
            new_QS = self.supply_func.evaluate_supply()
            new_eq_Quantity = min(new_QS, new_QD)
            self.new_eq_Quantity = min(new_QS, new_QD)
            self.new_eq_Point = [self.new_eq_Quantity, self.new_price]
            if not self.new_eq_efficiency():
                if new_QS < new_QD:
                    self.inefficency = "SHORTAGE"
                else:
                    self.inefficency = "SURPLUS"
            modify_price = 0

    def new_eq_efficiency(self):
        if self.new_price == self.equilibrium_price:
            return True
        else:
            return False

    def xDemand_upperBound(self):
        return sym.solve(self.demand_func, self.variables)[0]

    def ySupply_upperBound(self):
        return sym.solve(self.supply_func, self.variables)[0]

    def pEquilibrium(self):
        return sym.solve(self.demand_func - self.supply_func, p)[0]


A = SD(1000 - 25 * p, -200 + 50 * p)
print(A.demand_func, A.supply_func, A.variables, A.demand_price_zero, A.supply_quantity_zero, A.pEquilibrium(),
      A.equilibrium_quantity)
