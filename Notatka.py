class Notatka:
    __licznik = 0


    def __init__(self, tytul="", tresc=""):
        Notatka.__licznik += 1
        self._identyfikator = Notatka.__licznik
        self._tytul = tytul
        self._tresc = tresc


    def wyswietl(self):
        print (f'Tytuł: {self._tytul} \n Treść: \n {self._tresc}')

    def diagnostyka(self):
        print(f'{Notatka.__licznik}; {self._identyfikator}; {self._tytul} {self._tresc}')







# ‒ Klasa notatka zawiera jeden konstruktor o parametrach wejściowych dla tytułu i treści. Ma on za
# zadanie kolejno:
# ‒ inkrementować licznik notatek

# ‒ ustawić pola tytułu i treści równe parametrom
# ‒ Klasa notatka zawiera dwie metody bezparametrowe i niezwracające wartości, które mogą być
# wołane w programie głównym:
# ‒ metodę wyświetlenia tytułu i treści notatki
# ‒ metodę diagnostyczną wypisującą zawartości wszystkich pól oddzielone od siebie średnikami