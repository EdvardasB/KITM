import random
from typing import List

from model.Žmogus import Žmogus


class Šeima:
    žmonių_skaičius: int
    žmonės: List[Žmogus]

    def __init__(self, žmonių_skaičius=3, žmonės=None):
        self.žmonių_skaičius = žmonių_skaičius
        self.žmonės = žmonės

    def mock(self):
        žsk = random.randint(3, 5)
        self.žmonių_skaičius = žsk
        self.žmonės = [Žmogus() for _ in range(žsk)]
        return self