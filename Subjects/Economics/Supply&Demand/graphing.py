# importing the required module
import matplotlib
import matplotlib.pyplot as plt

# x axis values
quantity = [x for x in range(0,11)]
# corresponding y axis values
quantity_copied = quantity.copy()
supply = quantity_copied[::-1]
demand = quantity


# plotting the points
plt.plot(quantity, demand, color="blue",label="Demand")
plt.plot(quantity, supply,color="red",label="Supply")
plt.legend(loc="upper left")
# naming the x axis
plt.xlabel('Quantity')
# naming the y axis
plt.ylabel('Price')

# giving a title to my graph
plt.title('Supply and Demand Graph')

# function to show the plot
plt.show()f