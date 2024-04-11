from Notatka import Notatka

pierwszaNotatka = Notatka('Pierwsza notatka',
                          "Dyskografia O.S.T.R.-a – polskiego rapera i producenta muzycznego,"
                                               "obejmuje dziewiętnaście albumów solowych, "
                                               "jeden album koncertowy,"
                                               "trzydzieści dziewięć singli,"
                                               "siedem albumów we współpracy,"
                                               "cztery albumy specjalne oraz czterdzieści jeden teledysków." )
drugaNotatka = Notatka('Druga notatka',
                                        "Double Eagle –"
                                        "nazwa amerykańskich monet wykonanych ze złota o nominale 20 dolarów amerykańskich."
                                        "Były one uznane za prawny środek płatniczy w Stanach Zjednoczonych do 1933 roku.")

Notatka.wyswietl(pierwszaNotatka)
print("---------------------------------------------------------------")
Notatka.wyswietl(drugaNotatka)
