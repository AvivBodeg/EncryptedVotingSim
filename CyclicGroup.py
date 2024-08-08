import sympy
import math


class CyclicGroup:
    def __init__(self, n):
        self.n = n
        self.p = self._prime_finder()  # Amount of elements
        self.mod = 2 * self.p + 1  # mod parameter
        self.generator = self._generator_finder()
        self.elements = self._gen_cyclic_group_elements()

    def _prime_finder(self):
        """Finds a fitting prime number that can create a cyclic group with
        at least 2*n + 1 elements
        """
        p = sympy.nextprime(2 * self.n)
        while not sympy.isprime(2 * p + 1):
            p = sympy.nextprime(p)
        return p

    def _generator_finder(self):
        """Finds a suitable generator that can generate the cyclic group with
        returns -1 if a generator cannot be found
        """
        for i in range(2, self.mod - 1):
            if math.gcd(i, self.mod - 1) == 1:
                return i
        return -1

    def _gen_cyclic_group_elements(self):
        """Generates cyclic group elements"""
        cyclic_set = set()
        for i in range(self.p):
            cyclic_set.add(pow(self.generator, i, mod=self.mod))
        return cyclic_set
