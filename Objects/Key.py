import random
from CyclicGroup import CyclicGroup


def _gen_key(cyclic_group):
    key = random.randint(2, cyclic_group.mod - 2)
    return key


class Key:
    def __init__(self, cyclic_group: CyclicGroup):
        self.s_key = _gen_key(cyclic_group)
        self.p_key = pow(cyclic_group.generator, self.s_key, mod=cyclic_group.mod)
