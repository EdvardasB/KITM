"""
    1. Vartotojas:
        id
        Vardas
        Email
        Skelbimai
        Užklausos

        įdyti_skelbimą()
        ištrinti_skelbimą()
        redaguoti_skelbimą()
        ieškoti()
        užklausti()
        peržiūrėti_užklausas()
        patvirtinti_užklausą()
"""
from typing import List

from model.Skelbimas import Skelbimas
from model.Užklausa import Užklausa


class Vartotojas:
    vartotojo_id:str = None
    vardas:str = None
    email:str = None
    skelbimai:List[Skelbimas]
    užklausos:List[Užklausa]

    def __init__(self, vardas, email):
        self.vardas = vardas
        self.email = email