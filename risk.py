from random import random, normalvariate
from tools import run_or_eval


class Risk:
    def __init__(self, characteristic_a, characteristic_b, value, riskprocess):
        random_variables = {'u0': random(), 'u1': random(), 'u2': random(),
                            'n0': normalvariate(0, 1), 'n1': normalvariate(0, 1), 'n2': normalvariate(0, 1),
                            'v': value}
        self.a = run_or_eval(characteristic_a, random_variables)
        self.b = run_or_eval(characteristic_b, random_variables)
        self.probability = run_or_eval(riskprocess, {'a': self.a, 'b': self.b})
        self.time = 0
        while True:
            if random() < self.probability:
                break
            self.time += 1
        self.value = value

