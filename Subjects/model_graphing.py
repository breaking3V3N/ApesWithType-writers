# importing the required module
import matplotlib.pyplot as plt

p=5
q=4
"""
We meed to:
    (1)can graph wrt domain codomain 
"""
from model_functions import Demand, Supply

a = Demand()
b = Supply()


def find_eq(a: Demand, s: Supply):
    for x in range(0, len(a.codomain)):

        if a.codomain[x] == s.codomain[x]:
            return [a.domain[x], a.codomain[x]]
    return []


# print(find_eq(a, b))

def graph_setPrice(p: int, strp="P_0"):
    plt.plot(a.domain,len(a.domain) * [p],color="black",label=strp)

def graph_setQuantity(q: int, strq="Q_0"):
    plt.plot(len(a.domain) * [q],a.codomain, color="black", label=strq)

def graph_PriceIntercepts():
    for x in range(0, len(a.codomain)):
        if a.codomain[x] == p:
            return [a.domain[x], a.codomain[x]]
    plt.scatter()

def graph_quantityIntercepts():
    return [q,a.codomain[q]]

def graph_modelSandD(a: Demand, s: Supply):
    # plotting the points
    plt.plot(a.domain, a.codomain, color="blue", label=a.name)
    plt.plot(s.domain, s.codomain, color="red", label=s.name)

    # naming the x axis
    plt.xlabel("Quantity")
    # naming the y axis
    plt.ylabel("Price")

    # giving a title to my graph
    plt.title('Supply and Demand Graph')

    # label
    plt.text(a.domain[-1], a.codomain[-1], a.name)
    plt.text(s.domain[-1], s.codomain[-1], s.name)

    graph_setPrice(p)
    graph_setQuantity(q)
    eq_point = find_eq(a, s)
    """
    
    xlocs, xlabels = plt.xticks()
    np.append(xlocs,eq_point[0])
    np.append(xlabels,eq_point[1])
    plt.xticks(xlocs,xlabels)

    ylocs, ylabels = plt.yticks()
    np.append(ylocs, eq_point[0])
    np.append(ylabels,eq_point[1])
    plt.yticks(ylocs,ylabels)  
    """

    #Total eco activity
    plt.fill_between(a.domain[:6],s.codomain[:6], a.codomain[:6],color="red")
    #plt.fill_between(s.codomain[:5],a.codomain[:5], color="red")

    #Consumer Surplus
    plt.fill_between(a.domain[:6], p, a.codomain[:6], color="green")

    #Producer Surplus
    plt.fill_between(a.domain[:6], s.codomain[:6], p, color="yellow")

    # Product Surplus -- DO
    plt.fill_between(a.domain[:6], p, a.codomain[:6], color="green")

    # Product Shortage --DO
    plt.fill_between(a.domain[:6], s.codomain[:6], p, color="yellow")





    # plot eq
    # see if we need to do some form of plt. plot
    plt.scatter(eq_point[0], eq_point[1], label="EQ_1", color="black")

    # plot eq lines
    plt.vlines(eq_point[0], 0, eq_point[1], linestyles="dashed",label="EQ_1", color="black")
    plt.hlines(eq_point[0], 0, eq_point[1], linestyles="dashed", color="black")
    # key
    plt.legend(loc="upper left")

    # function to show the plot
    plt.show()


class Supply_and_Demand_Model:

    def __init__(self, d, s) -> None:
        """

        :param d:
        :param s:
        """
        self.demand = d
        self.supply = s
        self.eq_point = find_eq(self.demand, self.supply)


graph_modelSandD(a, b)
