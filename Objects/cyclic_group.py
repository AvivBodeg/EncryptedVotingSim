import sympy


class CyclicGroup:
    # set power between 20 and 24?
    SIZE_MULTIPLIER = pow(2, 23)

    def __init__(self, n: int):
        self.__n = n
        self.p = self.__prime_finder()  # Amount of elements
        self.mod = 2 * self.p + 1
        self.generator = 4
        self.elements = self.__gen_cyclic_group_elements()

    def __prime_finder(self):
        # Finds a fitting prime number that can create a cyclic group
        base = self.SIZE_MULTIPLIER  # minimum prime value
        p = sympy.nextprime(base)
        while not sympy.isprime(2 * p + 1):
            p = sympy.nextprime(p)
        return p

    def __gen_cyclic_group_elements(self):
        # Generates cyclic group elements
        cyclic_set = set()
        for i in range(self.p):
            cyclic_set.add(pow(self.generator, i, mod=self.mod))
        return cyclic_set
