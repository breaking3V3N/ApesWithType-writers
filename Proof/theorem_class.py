class Theorem:
    def __init__(self, given: str, show: str)->None:
        self.premises = given
        self.wts = show

    def