from typing import List, Union, Tuple

from model.Aukštas import Aukštas
from model.Individas import Individas
from model.Pora import Pora
from model.Šeima import Šeima


class Viešbutis:
    aukštų_skaičius: int
    aukštai: List[Aukštas]

    def __init__(self,
                 aukštų_skaičius,
                 apartamentų_info):
        self.aukštai = []
        apartamentų_skaičius_aukšte = sum([e[0] for e in apartamentų_info])
        for i in range(aukštų_skaičius):
            self.aukštai.append(Aukštas(i + 1, apartamentų_skaičius_aukšte, apartamentų_info))

    def __apgyvendinti(self, grupė: Union[Individas, Pora, Šeima]) \
            -> Tuple[bool, Union[Individas, Pora, Šeima]]:
        for aukštas in self.aukštai:
            if aukštas.ar_yra_laisvų_apartamentų():
                laisvi = aukštas.laisvi_apartamentai
                for apartamentai in laisvi:
                    apartamentai_apgyvendinti, grupė = apartamentai \
                        .apgyvendinti(grupė)
                    if apartamentai_apgyvendinti:
                        aukštas.uzimti_apartamentai.append(apartamentai)
                        aukštas.laisvi_apartamentai.remove(apartamentai)
                    if not grupė:
                        break
                if not grupė:
                    break
        return grupė is None, grupė

    def registratūra(self, keliaiviai: List[Union[Individas, Pora, Šeima]]):
        nepavyko = []
        for grupė in keliaiviai:
            pavyko_apgyvendinti, g = self.__apgyvendinti(grupė)
            if not pavyko_apgyvendinti:
                nepavyko.append(g)
        return nepavyko