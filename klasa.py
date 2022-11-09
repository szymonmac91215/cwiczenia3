class Klasa(object):
    tab = [1, 2, 3]

    def __init__(self, t, z1, z2):
        print('Wywołano metodę \'__init__()\'')
        self.tab = t
        self._zmienna1 = z1
        self.__zmienna2 = z2

    def print_z2(self):
        print(self.__zmienna2)

    def __del__(self):
        print('Wywołano metodę \'__del__()\'')

    def __str__(self):
        return 'Wywołano metodę \'__str__()\''

    def __repr__(self):
        return 'Wywołano metodę \'__repr__()\''

    def metodaInstancyjna(self):
        print('Wywołano metodę \'metodaInstancyjna()\'')
        print('klasowa -> ', self.__class__.tab)
        print('instancyjna -> ', self.tab)

    @classmethod
    def metodaKlasowa(cls):
        print('Wywołano metodę \'metodaKlasowa()\'')

    @staticmethod
    def metodaStatyczna():
        print('Wywołano metodę \'metodaStatyczna()\'')


# ( print(obiekt._Klasa__zmienna2) )
