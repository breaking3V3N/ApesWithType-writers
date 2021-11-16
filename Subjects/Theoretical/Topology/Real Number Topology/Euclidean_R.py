class subsets_of_r:

    def __init__(self, a: float, b: float, lower_boundary: bool, upper_boundary: bool) -> None:
        self.upper_bound = b
        self.lower_bound = a
        self.lower_boundary = lower_boundary
        self.upper_boundary = upper_boundary
        self.open = self.is_Open()
        self.closed = self.is_Closed()
        self.clopen = self.is_clopen()

    def is_in(self, x: float) -> bool:
        return self.isIn_interior(x) or self.isIn_boundary(x)

    def isIn_interior(self, x: float) -> bool:
        return self.lower_bound < x < self.upper_bound

    def isIn_boundary(self, x: float) -> bool:
        return x == self.lower_bound or x == self.upper_bound

    def is_Closed(self):
        return self.upper_bound or self.lower_bound

    def is_Open(self):
        return not (self.upper_bound or self.lower_bound)

    def is_clopen(self):
        return self.open and self.closed

    def is_intersect(self,other):
        if self.upper_bound < other

    def union(self,other):
        greatest_lower_bound = min(self.lower_bound,other.lower_bound)
        largest_upper_bound = max(self.upper_bound,other.upper_bound)

    def complement(self):
        return subsets_of_r()
