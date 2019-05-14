import time

from model.Skelbimas import Skelbimas
from model.Užklausa import Užklausa
from model.Vartotojas import Vartotojas


class DuomenųBazė:
    data = None

    def __init__(self):
        self.data = {}

    def save(self, object):
        try:
            getattr(self, type(object).__name__).append(object)
        except AttributeError:
            setattr(self, type(object).__name__, [object])

    def get_all(self, object_class):
        return getattr(self, object_class.__name__)


db = DuomenųBazė()
skelbimas = Skelbimas()
užklausa = Užklausa()
vartotojas = Vartotojas("Petras", "petras@gmail.com")

db.save(skelbimas)
db.save(užklausa)
db.save(vartotojas)

vartotojai = db.get_all(Vartotojas)

while True:
    time.sleep(1)
    request = input("Your code:\n")
    print(exec(request, globals()))
