import random

from model.Žmogus import Žmogus


class Individas(Žmogus):
    lytis: bool
    sutinka: bool

    def mock(self):
        self.lytis = random.choice([True, False])
        self.sutinka = random.choice([True, False])
        return self
