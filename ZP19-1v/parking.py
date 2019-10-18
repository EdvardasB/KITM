"""
AUTO PARKING
3 aukštų aikštelė
Aukšte yra 50 stovėjimo vietų
Aukštai žymimi raidėmis A-C
Vietos skaičiais 1-50

Stovėjimo kainos:
1h - 1 Eur
1h-6H - 0.7 Eur / h
6-24h - 0.5 Eur / h
>24h - 0.3 Eur / h

15min apvalinama į mažesnę pusę,
t.y. jeigu stovima 1val 15min, skaičiuojama už 1val.

Užduotis:
1) Paskirti stovėjimo vietą automobiliui
2) Aspkaičiuoti stovėjimo kainą
3) Apskaičiuoti dienos apyvartą

"""
from datetime import datetime
from random import choice, randint
from typing import List, Tuple

raidės = [chr(i) for i in range(ord("A"), ord("Z"))]
skaičiai = [str(n) for n in range(1, 10)]

šiandien = datetime(2019, 10, 18)


class VisosVietosUžimtos(Exception):
    pass


class Automobilis:
    automobilio_numeris: str
    atvyko: datetime
    išvyko: datetime

    def mock(self):
        numerių_raidės = "".join([choice(raidės) for _ in range(3)])
        numerių_skaičiai = "".join([choice(skaičiai) for _ in range(3)])
        self.automobilio_numeris = f"{numerių_raidės}:{numerių_skaičiai}"
        metai = šiandien.year
        mėnesis = šiandien.month
        diena = šiandien.day
        atvykimo_valanda = randint(0, 12)
        atvykimo_laikas = datetime(metai, mėnesis, diena, atvykimo_valanda)
        išvykimo_valanda = randint(atvykimo_valanda + 1, 23)
        išvykimo_laikas = datetime(metai, mėnesis, diena, išvykimo_valanda)
        self.atvyko = atvykimo_laikas
        self.išvyko = išvykimo_laikas


class Vieta:
    numeris: int
    užimta: bool = False
    stovinčio_automobilio_numeris: str = ""
    užimtumas: List[Tuple[datetime, datetime]]

    def __init__(self):
        self.užimtumas = []

    def priskirti_vietą(self, automobilis: Automobilis) -> bool:
        pavyko_priskirti = False
        if not self.užimta or self.užimtumas[-1][1] < automobilis.atvyko:
            self.stovinčio_automobilio_numeris = automobilis.automobilio_numeris
            self.užimtumas.append((automobilis.atvyko, automobilis.išvyko))
            self.užimta = True
            pavyko_priskirti = True
        return pavyko_priskirti

    def __repr__(self):
        if self.užimta:
            return f"class<Vieta> Taken by:{self.stovinčio_automobilio_numeris}"
        else:
            return f"class<Vieta> Free"


class Aukštas:
    aukšto_raidė: str
    vietų_skaičius: int
    vietos: List[Vieta]

    def __init__(self, vietų_aukšte_skaičius):
        self.vietų_skaičius = vietų_aukšte_skaičius
        self.vietos = []
        for i in range(vietų_aukšte_skaičius):
            vieta = Vieta()
            vieta.numeris = i + 1
            self.vietos.append(vieta)

    def paskirti_vietą(self, automobilis) -> bool:
        pavyko_priskirti = False
        for vieta in self.vietos:
            pavyko_priskirti = vieta.priskirti_vietą(automobilis)
            if pavyko_priskirti:
                break
        return pavyko_priskirti

    def __repr__(self):
        return f"class<Aukštas>Symbol:{self.aukšto_raidė} | Capacity:{self.vietų_skaičius}"


class StovėjimoAikštelė:
    aukštai: List[Aukštas]

    def __init__(self, aukštų_skaičius, vietų_aukšte_skaičius):
        self.aukštai = []
        for i in range(aukštų_skaičius):
            aukštas = Aukštas(vietų_aukšte_skaičius)
            aukštas.aukšto_raidė = raidės[i]
            self.aukštai.append(aukštas)

    def paskirti_stovėjimo_vietą(self, automobilis: Automobilis):
        pavyko = False
        for aukšas in self.aukštai:
            pavyko = aukšas.paskirti_vietą(automobilis)
            if pavyko:
                break
        if not pavyko:
            raise VisosVietosUžimtos("Atsiprašome, visos vietos užimtos.")


stovėjimo_aikštelė = StovėjimoAikštelė(3, 50)
for _ in range(1000):
    automobilis = Automobilis()
    automobilis.mock()
    try:
        stovėjimo_aikštelė.paskirti_stovėjimo_vietą(automobilis)
    except VisosVietosUžimtos:
        print("Sėkmingai handlintas exceptionas")
if __name__ == '__main__':
    pass
