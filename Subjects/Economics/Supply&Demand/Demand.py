from enum import IntEnum as Enum
import matplotlib.pyplot as plt


class demandFunctions(Enum):
    Arbitrary: 1
    #Particular is for numeric
    Particular: 2

class demandForces(Enum):
    TasteShift: "a"
    PopulationTendencyToBuy: "b"
    Income: "c"
    priceOfSubstitute: "d"
    priceOfComplement: "e"
    futureExpec: "f"


class direction(Enum):
    Increase: 1
    Decrease: -1


class Demand:


    def __init__(self, Demand_vals=[x for x in range(0, 11)]):
        self.d_state = 0
        self.demand_vals = Demand_vals
        #self.type = dtype
        # self.d_func =

    def demand_change(self, direc_movement: direction):
        self.d_state + direc_movement
        d_prime = [x - direc_movement * 2 for x in self.demand_vals]
        return Demand(d_prime)
    21




# x axis values
quantity = [x for x in range(0, 11)]
# corresponding y axis values
quantity_copied = quantity.copy()
supply = quantity_copied[::-1]
demand = quantity


d_0 = Demand(demand)
d_1 = d_0.demand_change(1)
d_1prime = d_1.demand_vals

# plotting the points
plt.plot(quantity, d_1prime, color="purple", label="D_1")
plt.plot(quantity, demand, color="blue", label="D_0")
plt.plot(quantity, supply, color="red", label="Supply")
plt.legend(loc="upper left")
# naming the x axis
plt.xlabel('Quantity')
# naming the y axis
plt.ylabel('Price')

# giving a title to my graph
plt.title('Supply and Demand Graph')

# Setting limits for X and Y axis
plt.xlim([0,10])
plt.ylim([0,10])


plt.annotate("Q_P",(5,5))

# function to show the plot
plt.show()
