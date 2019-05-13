from typing import List, Tuple

from model.Apartamentai import Apartamentai


class Aukštas:
    numeris: int
    apartamentų_skaičius: int
    laisvi_apartamentai: List[Apartamentai]
    uzimti_apartamentai: List[Apartamentai]

    def __init__(self, numeris, apartamentų_skaičius, info: List[Tuple[int, int]]):
        self.numeris = numeris
        self.apartamentų_skaičius = apartamentų_skaičius
        self.laisvi_apartamentai = []
        self.uzimti_apartamentai = []
        apartamento_nr = iter(list(range((numeris - 1) * apartamentų_skaičius + 1,
                                         numeris * apartamentų_skaičius + 1)))
        for n, vietų_skaičius in info:
            for i in range(n):
                self.laisvi_apartamentai \
                    .append(Apartamentai(next(apartamento_nr), vietų_skaičius))

    def ar_yra_laisvų_apartamentų(self) -> bool:
        if self.laisvi_apartamentai:
            return True
        return False
