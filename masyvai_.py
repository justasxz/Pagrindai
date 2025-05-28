# sarasas = [] # Sukuriamas tuščias sąrašas

# sarasas = [4,1,7,5,8] # Sukuriamas sąrašas su penkiais elementais | list tipo

# print(sarasas) # Išvedamas sąrašas

# sarasas.append(7) # Pridedamas elementas 7 prie sąrašo pabaigos
# print(sarasas) # Išvedamas sąrašas su nauju elementu

# print(sarasas[3]) # Išvedamas ketvirtas elementas sąraše (indeksas 3)
# # programavime skaičiuojama nuo 0, todėl pirmas elementas yra indeksu 0, antras 1 ir t.t.

# # print(sarasas[5]) # index out of range - klaida, nes sąraše nėra šešto elemento (indeksas 5)

# # CRUD operacijos:
# # Create - sukurti
# # Read - nuskaityti
# # Update - atnaujinti
# # Delete - ištrinti

# sarasas.remove(7) # Ištrinama pirmoji 7 reikšmė iš sąrašo
# print(sarasas) # Išvedamas sąrašas be 7 reikšmės
# sarasas.pop(0) # Ištrinama pirmoji reikšmė iš sąrašo (indeksas 0)

# print(sarasas) # Išvedamas sąrašas be pirmos reikšmės

# sarasas = [4,1,7,5,8]
# sarasas[3] = 10 # Atnaujinama ketvirto elemento reikšmė į 10
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšme

# Saraso CRUD
# sarasas = [4,1,7,5,8]
# sarasas.append(7) # Pridedamas elementas 7 prie sąrašo pabaigos
# print(sarasas) # Išvedamas sąrašas su nauju elementu
# sarasas.remove(7) # Ištrinama pirmoji 7 reikšmė iš sąrašo
# print(sarasas) # Išvedamas sąrašas be 7 reikšmės
# sarasas.pop(0) # Ištrinama pirmoji reikšmė iš sąrašo (indeksas 0)
# print(sarasas) # Išvedamas sąrašas be pirmos reikšmės
# sarasas[3] = 10 # Atnaujinama ketvirto elemento reikšmė į 10
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšmė

# zodziai = ["labas", "rytas", "pasauli", "kaip", "sekasi"]
# print(zodziai[0]) # Išvedamas pirmas žodis sąraše
# skaiciai = [1, 2, 3, 4, 5]
# floatai = [1.5, 2.5, 3.5, 4.5, 5.5]
# booleans = [True, False, True, False, True]
# mixuotas = [1, "labas", 2.5, True, "rytas"] # nerekomenduotina naudoti, bet galima


# sarasas = [4,1,7,5,8,1,2,3,4]
# sarasas.pop(2)
# print(sarasas) # Išvedamas sąrašas su atnaujinta reikšme
# saraso_ilgis = len(sarasas) # Apskaičiuojamas sąrašo ilgis (elementų skaičius)
# print(saraso_ilgis) # Išvedamas sąrašo ilgis (elementų skaičius)
# print(sarasas(5))


# sarasas = [4,1,7,5,8,1,2,3,4]

# sakinys = "Sveiki studentai, tikiuosi, kad jums sekasi gerai"

# # print(sakinys[10]) # Išvedamas pirmas simbolis sakinyje

# # Pagrindinis skirtumas tarp string ir saraso yra, tas, kad string yra immutable, o sarasas yra mutable
# # sakinys[5] = "a" # TypeError: 'str' object does not support item assignment

# # slicing
# # print(sakinys[0:5]) # Išvedamas pirmas 5 simboliai sakinyje | pirmas elementas ieina o antras nera imtinai
# print(sakinys[-3]) # minus reiskia nuo antro galo
# print(sakinys[5:]) # Išvedamas simboliai nuo 5 iki galo
# print(sakinys[:5]) # Išvedamas simboliai nuo pradzios iki 5
# print(sakinys[-10:-3]) # geriau privengti, nes sudetinga skaityti
# print(sakinys[::-1]) # sarasas[start:stop:step] 
# print(sakinys[::2]) 
# print(sakinys[5:20:2]) # Išvedamas simboliai nuo 5 iki 20 kas antras


