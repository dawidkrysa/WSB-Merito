# Author: Dawid Krysa
# Repository: https://github.com/dawidkrysa/WSB-Merito

import numpy as np

# Zadanie 6 (2.16)
#
# Strukturę bezrobotnych zarejestrowanych w Polsce w 1993 roku (stan na 31.12)
# według wieku i płci przedstawiono w tablicy:
#
# Źródło: Rocznik Statystyczny 1994, GUS, tabl. 25(209), s. 129.
#
# a) Porównać przeciętny wiek bezrobotnych kobiet i mężczyzn.
# b) Jaki był przeciętny wiek bezrobotnych zarejestrowanych w Polsce
#    31.12.1993 roku?

# Grupy wiekowe [lata]
wiek = np.array(
    [
        "poniżej 25",
        "25-34",
        "35-44",
        "45-54",
        "55 i więcej",
    ]
)

# Liczba bezrobotnych [tys.]
kobiety = np.array(
    [
        524.3,
        455.1,
        382.8,
        132.0,
        13.1,
    ]
)

mezczyzni = np.array(
    [
        471.7,
        369.6,
        346.3,
        152.2,
        43.5,
    ]
)


print("""---------------------------------------------------------------
a) Porównać przeciętny wiek bezrobotnych kobiet i mężczyzn.
---------------------------------------------------------------""")
# Granice przedziałów wieku [lata]
# Kobiety: 18-60, mężczyźni: 18-65 (wiek produkcyjny)
# Przedziały traktuję jako ciągłe: 18-25, 25-35, 35-45, 45-55, 55-60/65
dolne_k = np.array([18, 25, 35, 45, 55])
gorne_k = np.array([25, 35, 45, 55, 60])

dolne_m = np.array([18, 25, 35, 45, 55])
gorne_m = np.array([25, 35, 45, 55, 65])

# Środki przedziałów
srodki_k = (dolne_k + gorne_k) / 2
srodki_m = (dolne_m + gorne_m) / 2

suma_k = np.sum(srodki_k * kobiety)
suma_m = np.sum(srodki_m * mezczyzni)

sr_k = suma_k / np.sum(kobiety)
sr_m = suma_m / np.sum(mezczyzni)

print(f"Kobiety:    {sr_k:.2f} lat")
print(f"Mężczyźni:  {sr_m:.2f} lat")
print(f"Różnica:    {sr_m - sr_k:.2f} lat")

print("""
---------------------------------------------------------------
b) Jaki był przeciętny wiek bezrobotnych zarejestrowanych w Polsce
   31.12.1993 roku?
---------------------------------------------------------------""")
sr_wszyscy = (suma_k + suma_m) / (np.sum(kobiety) + np.sum(mezczyzni))
print(f"Przeciętny wiek bezrobotnych: {sr_wszyscy:.2f}")
