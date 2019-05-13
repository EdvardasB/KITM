import random
from typing import Union, List

from model.Individas import Individas
from model.Pora import Pora
from model.Šeima import Šeima


class Autobusas:
    keleivių_skaičius: int
    keleiviai: List[Union[Individas, Pora, Šeima]]

    def __init__(self, keleivių_skaičius):
        self.keleivių_skaičius = keleivių_skaičius
        n = 0
        self.keleiviai = []
        while n < keleivių_skaičius:
            grupės_klasė = random.choice([Individas, Pora, Šeima])
            grupė = grupės_klasė().mock()
            if isinstance(grupė, (Pora, Šeima)):
                if n + grupė.žmonių_skaičius <= keleivių_skaičius:
                    n += grupė.žmonių_skaičius
                    self.keleiviai.append(grupė)
            else:
                n += 1
                self.keleiviai.append(grupė)
