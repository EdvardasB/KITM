import random

from model.Autobusas import Autobusas
from model.Viešbutis import Viešbutis

viesbutis = Viešbutis(20, [(2, 5), (3, 4), (3, 2)])
autobusai = []
n = 0
while True:
    autobusas = Autobusas(random.randint(30, 40))
    nepavyko = viesbutis.registratūra(autobusas.keleiviai)
    if nepavyko:
        print("Nepavyko apgyvendinti")
        break
    else:
        autobusai.append(autobusas)
        n += 1
        print(f"Apgyvendintas {n} autobusas")
if __name__ == '__main__':
    pass
