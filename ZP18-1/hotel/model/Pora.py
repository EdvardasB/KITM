from typing import List

from model.Žmogus import Žmogus


class Pora:
    žmonių_skaičius: int = 2
    žmonės: List[Žmogus]

    def mock(self):
        self.žmonės = [Žmogus() for _ in range(2)]
        return self
