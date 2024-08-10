import sympy
import math
import random


class CyclicGroup:
    SIZE_MULTIPLIER = 10000

    def __init__(self, n: int):
        self.__n = n
        self.p = self.__prime_finder()  # Amount of elements
        self.mod = 2 * self.p + 1  # Modulo parameter
        self.generator = self.__generator_finder()
        self.elements = self.__gen_cyclic_group_elements()

    def __prime_finder(self):
        """Finds a fitting prime number that can create a cyclic group with
        at least 2*n + 1 elements
        """
        base = SIZE_MULTIPLIER = 10000  # minimum prime value
        p = sympy.nextprime(base)
        while not sympy.isprime(2 * p + 1):
            p = sympy.nextprime(p)
        return p

    def __generator_finder(self):
        """Finds a suitable generator that can generate the cyclic group with
        returns -1 if a generator cannot be found
        """
        for i in range(2, self.mod - 1):
            if math.gcd(i, self.mod - 1) == 1:
                return i
        return -1

    def __gen_cyclic_group_elements(self):
        """Generates cyclic group elements"""
        cyclic_set = set()
        for i in range(self.p):
            cyclic_set.add(pow(self.generator, i, mod=self.mod))
        return cyclic_set


def main():
    group = CyclicGroup(100)


if __name__ == "__main__":
    main()
