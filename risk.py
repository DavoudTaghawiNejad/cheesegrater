from random import random
from tools import run_or_eval


class Risk:
    def __init__(self, a, b, value, riskprocess):
        self.probability = run_or_eval(riskprocess, {'a': a, 'b': b})
        self.time = 0
        while True:
            if random() < self.probability:
                break
            self.time += 1
        self.value = value
        self.a = a
        self.b = b

