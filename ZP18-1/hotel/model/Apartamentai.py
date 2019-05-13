from typing import Union, List, Tuple

from model.Individas import Individas
from model.Pora import Pora
from model.Šeima import Šeima


class Apartamentai:
    numeris: int
    vietų_skaičius: int
    gyvena: Union[List[Individas], Pora, Šeima] = None
    užimtas: bool = False

    def __init__(self, numeris, vietų_skaičius):
        self.numeris = numeris
        self.vietų_skaičius = vietų_skaičius

    def __ar_galima_apgyvendinti(self, individas):
        lytis = individas.lytis
        for gyventojas in self.gyvena:
            if gyventojas.lytis != lytis and not gyventojas.sutinka:
                return False
        return True

    def apgyvendinti(self, grupė: Union[Individas, Pora, Šeima]) -> Tuple[
        bool, Union[Individas, Pora, Šeima, None]]:
        if isinstance(grupė, (Šeima, Pora)):
            if not self.gyvena and self.vietų_skaičius >= grupė.žmonių_skaičius:
                self.gyvena = grupė
                self.užimtas = True
                return True, None
            else:
                return False, grupė

        if isinstance(grupė, Individas):
            individas = grupė
            if not self.gyvena:
                self.gyvena = [individas]
                return True, None
            elif self.__ar_galima_apgyvendinti(individas):
                self.gyvena.append(individas)
                if len(self.gyvena) == self.vietų_skaičius:
                    self.užimtas = True
                return True, None
            return False, individas

