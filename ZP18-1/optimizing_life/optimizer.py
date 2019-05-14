"""
Gyvenimo optimizavimas

1) Svertai
2) Veiklos
3) Grafiko sudarymas
4) Svertų patikrinimas/perskaičiavimas

"""
from typing import List, Dict, Tuple


class Veikla:
    pavadinimas: str
    kategorija: str
    svarba: int
    ar_fiksuotas_laikas: bool
    laikas: float
    min_laikas: float
    max_laikas: float
    išlaidos: float
    fiksuotas_kiekis_per_laiko_tarpą: Tuple[float, str]


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




Tadas = Asmuo("Tadas")
Tadas.darbas = 9.0
Tadas.miegas = 6.0
Tadas.kelionių_laikas = 1.0
print(f"Laisvas laikas: {Tadas.laisvas_laikas}")
Tadas.laisvas_laikas = 10
