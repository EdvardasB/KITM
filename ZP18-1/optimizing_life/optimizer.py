"""
Gyvenimo optimizavimas

1) Svertai
2) Veiklos
3) Grafiko sudarymas
4) Svertų patikrinimas/perskaičiavimas

"""
from typing import List, Dict, Tuple


def Builder(C):
    def wrapper(attr):
        def builder(self, value):
            setattr(self, attr, value)
            return self

        return builder

    annotations = C.__annotations__
    for attr, attr_type in annotations.items():
        if attr_type == bool:
            setattr(C, f"is_{attr}", wrapper(attr))
        else:
            setattr(C, f"with_{attr}", wrapper(attr))
    return C


@Builder
class Veikla:
    pavadinimas: str
    kategorija: str
    svarba: int
    ar_fiksuotas_laikas: bool
    laikas: float
    min_laikas: float
    max_laikas: float
    išlaidos: float

    def __repr__(self):
        return f"Veikla<{self.pavadinimas}>"

    def __init__(self,
                 pavadinimas,
                 kategorija,
                 svarba,
                 ar_fiksuotas_laikas,
                 išlaidos=0.0):
        self.pavadinimas = pavadinimas
        self.kategorija = kategorija
        self.svarba = svarba
        self.ar_fiksuotas_laikas = ar_fiksuotas_laikas
        self.išlaidos = išlaidos


class Asmuo:
    biudžetas: float = None
    vardas: str = None
    veiklos: List[Veikla] = None
    svertai: Dict[str, float] = None
    miegas: float
    darbas: float
    kelionių_laikas: float

    def __init__(self, vardas):
        self.vardas = vardas
        self.svertai = {
            "Pramogos": 0.25,
            "Poilsis": 0.25,
            "Socializacija": 0.25,
            "Tobulėjimas": 0.25
        }

    @property
    def laisvas_laikas(self):
        return 24 - self.miegas - self.darbas - self.kelionių_laikas

    @laisvas_laikas.setter
    def laisvas_laikas(self, laikas):
        print("Laisvo laiko negalima nustatyti. "
              "Jis apskaičiuojamas iš 24val atėmus darbo, miego, "
              "bei kelionių laiką."
              )

    @property
    def grafikas(self) -> List[Tuple[float, Veikla]]:
        pasirinktos_veiklos = []
        laisvas_laikas = self.laisvas_laikas
        laisvas_laikas_kategorijai = {}
        for kategorija, svertas in self.svertai.items():
            laisvas_laikas_kategorijai[kategorija] = laisvas_laikas * svertas
        for kategorija, laikas in laisvas_laikas_kategorijai.items():
            veiklos = [veikla for veikla in self.veiklos
                       if veikla.kategorija == kategorija]
            veiklos.sort(key=lambda v: v.svarba, reverse=True)
            for veikla in veiklos:
                if veikla.ar_fiksuotas_laikas and laikas >= veikla.laikas:
                    pasirinktos_veiklos.append((veikla.laikas, veikla))
                    laikas -= veikla.laikas
                if not veikla.ar_fiksuotas_laikas \
                        and veikla.min_laikas <= laikas:
                    if laikas >= veikla.max_laikas:
                        pasirinktos_veiklos.append((veikla.max_laikas, veikla))
                        laikas -= veikla.max_laikas
                    else:
                        pasirinktos_veiklos.append((laikas, veikla))
                        laikas = 0
                if laikas == 0:
                    break
        return pasirinktos_veiklos


v1 = Veikla("Sporto klubas", "Pramogos", 10, False) \
    .with_min_laikas(1) \
    .with_max_laikas(3)
v2 = Veikla("Baseinas", "Pramogos", 20, True) \
    .with_laikas(1)
v3 = Veikla("Susitikimas su draugais", "Socializacija", 10, False) \
    .with_min_laikas(1) \
    .with_max_laikas(3)
v4 = Veikla("Skaitymas", "Tobulėjimas", 10, True) \
    .with_laikas(1)
v5 = Veikla("Programavimas", "Tobulėjimas", 20, True) \
    .with_laikas(1)
v6 = Veikla("TV", "Poilsis", 10, True) \
    .with_laikas(1)

Tadas = Asmuo("Tadas")
Tadas.darbas = 9.0
Tadas.miegas = 6.0
Tadas.kelionių_laikas = 1.0
Tadas.veiklos = [v1, v2, v3, v4, v5, v6]
print(f"Laisvas laikas: {Tadas.laisvas_laikas}")
print("Grafikas")
for item in Tadas.grafikas:
    print(item)