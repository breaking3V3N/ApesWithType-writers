from Demand import direction

class Supply:

    def __init__(self, Supply_vals=[x for x in range(0, 11)]):
        self.s_state = 0
        self.supply_vals = Supply_vals
        #self.type = dtype
        # self.d_func =

    def demand_change(self, direc_movement: direction):
        self.s_state + direc_movement
        s_prime = [x - direc_movement * 2 for x in self.supply_vals]
        return Supply(s_prime)

