"""



"""


class Topology:

    def __init__(self, X: set, tau:set):
        self.set = X
        self.tau = tau

    def containment(self):
        return self.set in self.tau and "empty" in self.tau

    def closure_union(self):
        for open_set in self.tau:
            new_tau = self.tau
            new_tau.remove(open_set)
            for element in new_tau:
                if element.union(open_set) not in self.tau:
                    return False
        return True

    def closure_intersection(self):
        for open_set in self.tau:
            new_tau = self.tau
            new_tau.remove(open_set)
            for element in new_tau:
                if element.intersect(open_set) not in self.tau:
                    return False
        return True

