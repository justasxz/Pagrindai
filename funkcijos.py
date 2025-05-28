

# def spausdinti_teksta(tekstas):
#     """
#     Funkcija spausdina teksta.
#     :param tekstas: Tekstas, kuris bus spausdinamas.
#     """
#     print('='*40)
#     print(tekstas)
#     print('='*40)

# spausdinti_teksta('Labas rytas!')
# spausdinti_teksta('Labas vakaras!')
# spausdinti_teksta('Labas naktis!')


# def pakelti_kvadrata(n): # n = 5
#     """
#     Funkcija pakelia skaičių kvadratu.
#     :param n: Skaičius, kurį reikia pakelti kvadratu.
#     :return: Pakeltas kvadratu skaičius.
#     """
#     return n ** 2

# pakelti_kvadrata(5) # vietoje funkcijos atsistoja 5^2 = 25


# 25

# def pasisveikinti(vardas, pavarde):
#     """
#     Funkcija pasisveikina su žmogumi.

#     :param vardas: Zmogaus vardas su kuriuo sveikinames.

#     :param pavarde: Pavardė.

#     """
#     print(f'Labas, {vardas} {pavarde}!')
#     # jeigu nera returno galima isvaizduoti, kad programa automatiskai padaro
#     # return None

# pasisveikinti('Jonas', 'Jonaitis')
# None # jis dar ivyko print savo viduje
# pasisveikinti('Petras', 'Petraitis')
# pasisveikinti('Ona', 'Onaitė')
# pasisveikinti('Marytė', 'Marytė')

# value ir reference argumentai



# def spausdinti_teksta(tekstas):
#     print('='*40)
#     print(tekstas)
#     print('='*40)

# spausdinti_teksta("Tekstinis") 

# def kvadratu(x): # x yra naujas lokalus (funkcijos ribose) kintamasis, kuris sukuriamas iskvieciant funkcija # kintamieji yra lokalus ir globalus
#     x = x ** 2
#     return x

# x = 5
# print(x)
# rezultatas = kvadratu(x)
# print(x) 

# print(rezultatas) # 25


# def kvadratu(sk): # sk = 5 
#     sk = sk ** 2
#     return sk

# x = 5
# print(x)
# rezultatas = kvadratu(x)

# print(x) 

# print(rezultatas) # 25



# def grazink_skaiciu():
#     return 5,9,4

# print(grazink_skaiciu()) 


# def pakelti_sarasa_laipsniu(sarasas, laipsnis):
#     """
#     Funkcija pakelia kiekvieną skaičių sąraše kvadratu.

#     :param sarasas: Sąrašas, kurį reikia pakelti kvadratu.
#     :return: Naujas sąrašas su pakeltais kvadratu skaičiais.
#     """
#     index = 0
#     while index < len(sarasas):
#         sarasas[index] = sarasas[index] ** laipsnis # sarasas[0] = sarasas[0] ** 2 | sarasas[1] = sarasas[1] ** 2 | sarasas[2] = sarasas[2] ** 2
#         index += 1


# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# pakelti_sarasa_laipsniu(my_list,3)
# print(my_list)


# def kvadratu(x): # x = 5
#     """
#     Funkcija pakelia skaičių kvadratu.

#     :param x: Skaičius, kurį reikia pakelti kvadratu.
#     :return: Pakeltas kvadratu skaičius.
#     """
#     return x ** 2

# sk = 5
# print(kvadratu(sk)) # 25
# print(sk)

# def prideti_elementa(sarasas): # sarasas = 0x7f8c4c0b3d90
#     sarasas.append(5) 
#     return sarasas

# my_list = [1, 2, 3, 4] # my_list = 0x7f8c4c0b3d90
# print(my_list) # [1, 2, 3, 4]
# prideti_elementa(my_list) # [1, 2, 3, 4, 5]
# print(my_list) # [1, 2, 3, 4, 5]



# def grazinti_rezultata(kint):
#     if kint > 0:
#         return True # bool
#     elif kint < 0:
#         return False # string
#     else:
#         raise ValueError("Nulis") # klaida



# def skaiciavimo_funkcija(skaicius,daugiklis=1,pridetis=0,nebutinas=4):
#     return (skaicius * daugiklis) + pridetis 


# print(skaiciavimo_funkcija(7))

# def neribota_suma(*skaiciai): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.

#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius
#     return suma

# print(neribota_suma(9,4,5,8,7,89,5,4,5,1,4,8,6))

# def neribota_suma(skaiciai): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.

#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius
#     return suma

# print(neribota_suma([9,4,5,8,7,89,5,4,5,1,4,8,6]))

# def spausdinti_neribota_teksta(**tekstas): # **tekstas = {'vardas': 'Jonas', 'pavarde': 'Jonaitis'}
#     """
#     Funkcija, kuri spausdina neribotą skaičių argumentų.

#     :param tekstas: Neribotas skaičių argumentų kiekis.
#     """
#     for raktas, reiksme in tekstas.items():
#         print(f'{raktas}: {reiksme}')


# spausdinti_neribota_teksta(vardas='Jonas', pavarde='Jonaitis', amzius=30, miestas='Vilnius')

# def spausdinti_neribota_teksta(tekstas): # **tekstas = {'vardas': 'Jonas', 'pavarde': 'Jonaitis'}
#     """
#     Funkcija, kuri spausdina neribotą skaičių argumentų.

#     :param tekstas: Neribotas skaičių argumentų kiekis.
#     """
#     for raktas, reiksme in tekstas.items():
#         print(f'{raktas}: {reiksme}')


# spausdinti_neribota_teksta({'vardas': 'Jonas', 'pavarde': 'Jonaitis', 'amzius': 30, 'miestas': 'Vilnius'})

# def neribota_suma(*skaiciai,daugiklis): # is esmes zvaigzdute tiesiog sukuria tupla, kurioje yra visi argumentai | skaiciai = [9,4,5,8,7,89,5,4,5,1,4,8,6]
#     """
#     Funkcija, kuri priima neribotą skaičių argumentų ir grąžina jų sumą.

#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Skaičių suma.
#     """
#     suma = 0
#     for skaicius in skaiciai:
#         suma += skaicius * daugiklis
#     return suma

# print(neribota_suma(9,4,5,8,7,89,5,4,5,1,4,8,6,daugiklis=2)) 

# def sumuoti(skaiciu_sarasas : list) -> int:
#     """
#     Funkcija, kuri apskaičiuoja sumą.

#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Suma.
#     """
#     suma = 0
#     for skaicius in skaiciu_sarasas:
#         suma += skaicius
#     return suma

# def vidurkis(*skaiciai):
#     """
#     Funkcija, kuri apskaičiuoja vidurkį.

#     :param skaiciai: Neribotas skaičių kiekis.
#     :return: Vidurkis.
#     """
#     grazinta_suma = sumuoti(skaiciai)
#     kiekis = len(skaiciai)
#     return grazinta_suma / kiekis if kiekis > 0 else 0

# print(sumuoti([1, 2, 3, 4, 5])) # 15
# print(vidurkis(1, 2, 3, 4, 5)) # 3.0

# def grazinti_pagal_salyga(x):
#     """
#     Funkcija, kuri grąžina skaičių pagal tam tikrą sąlygą.

#     :param x: Skaičius, kurį reikia patikrinti.
#     :return: Grąžina skaičių pagal sąlygą.
#     """
#     if x > 0:
#         return True
#     elif x < 0:
#         return False
#     else:
#         raise ValueError("Nulis") # klaida
# funkcija grazina kelias reiksmes
# def grazinti_kelis(x):
#     """
#     Funkcija, kuri grąžina kelis skaičius.

#     :param x: Skaičius, kurį reikia patikrinti.
#     :return: Grąžina kelis skaičius.
#     """
#     if x > 0:
#         return 1,2,3
#     elif x < 0:
#         return  -1, -2, -3
#     else:
#         raise ValueError("Nulis") # klaida
    
# print(grazinti_kelis(5))

# def grazink_du():
#     """
#     Funkcija, kuri grąžina du skaičius.
#     """
#     return 5, 9

# a,b = grazink_du() # grazina tuple (5, 9)
# print(a) # 5
# print(b) # 9
# print(grazink_du()) # grazina tuple

# "sda".strip()

# def spausdinti_teksta(tekstas : str) -> str:
#     return f'{"="*40}\n{tekstas}\n{"="*40}'

# spausdinti_teksta(213)

# def kubu(skaicius):
#     return skaicius ** 3


# funkcijos_kint = lambda skaicius: print(skaicius ** 3 * 5 + 2)


# funkcijos_kint(5)
# funkcijos_kint(5)

import time

sarasas = range(1,20000)

start = time.perf_counter()

naujas_sarasas = []

for i in sarasas:
    naujas_sarasas.append(i ** 2)

# print(naujas_sarasas) 

end = time.perf_counter()
print(f'for ciklas uztruko {(end - start)*1000} ms.')

start = time.perf_counter()
naujas_map_sarasas = list(map(lambda x: x ** 2, sarasas)) # tas pats kas for ciklas, tik trumpesnis plius lambada funkcija, 
# print(naujas_map_sarasas)
    
end = time.perf_counter()
print(f'map uztruko {(end - start)*1000} ms.')