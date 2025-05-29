# tuscas_zodynas = {} # tuscias zodynas
# zodynas = {"Lietuva":"Vilnius", # Lietuva - raktas(key), Vilnius - reikšmė(value)
#             "Latvija":"Riga",
#             "Estija":"Talinas",
#             "Lenkija":"Varšuva",
#             "Vokietija":"Berlynas",
#             "Prancūzija":"Paryžius"}
# print(zodynas)
# # zodyne skirtingai nei sarase viskas vyksta aplink raktus nera indeksu

# print(zodynas["Estija"])
# print(zodynas["Lietuva"])

# zodynas["Ispanija"] = "Madridas" # Pridedamas naujas raktas ir reikšmė
# print(zodynas) # Išvedamas zodynas su nauju raktu ir reikšme

# zodynas["Lietuva"] = "Kaunas" # Atnaujinama reikšmė pagal raktą
# print(zodynas) # Išvedamas zodynas su atnaujinta reikšme
# # jeigu raktas jau yra zodyne tai jis atnaujina reiksme, jeigu nera tai prideda nauja raktas-reiksme

# zodynas["Lietuva"] = zodynas["Lietuva"].upper() # Atnaujinama reikšmė pagal raktą
# print(zodynas)

# zodynas.pop("Estija") # Ištrinamas raktas ir reikšmė pagal raktą
# print(zodynas) # Išvedamas zodynas be ištrinto rakto ir reikšmės

# del zodynas["Latvija"] # Ištrinamas raktas ir reikšmė pagal raktą, rečiausiai naudojamas
# print(zodynas) # Išvedamas zodynas be ištrinto rakto ir reikšmės




# sakinys = "Sveiki studentai, tikiuosi, kad jums sekasi gerai" # o jeigu naudotojas iveda kitoki sakini ? 

# sarasas = sakinys.split(',') # split padalina sakini i zodzius pagal tarpa | sarasas = ["Sveiki", "studentai,", "tikiuosi,", "kad", "jums", "sekasi", "gerai"]
# print(sarasas)
# print(sarasas[1])

# setas = {1,1,2,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7} # setas - unikalus elementai, nera pasikartojimu
# print(setas)

# # turite sarasa su pasikartojanciais elementais, atrinkite tik unikalius elementus

# sarasas = [1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8] # sarasas su pasikartojanciais elementais
# print(sarasas) # Išvedamas sąrašas su pasikartojančiais elementais
# # int(input("Tekstas"))
# atrinkti = set(sarasas)
# print(atrinkti)

# tuplas = (1,2,3,4,5) # tuplas - nekeičiama sekos struktūra, panaši į sąrašą, bet negalima keisti elementų

# print(tuplas) # Išvedamas tuplas, tuplas naudojamas nes, `jeigu reikia, kad elementai butu nekeičiami`
# tuplas[0] = 10 # Išmetama klaida, nes tuplas yra nekeičiama sekos struktūra

# set - {}, tuple -(), list - [], dict - {key:value}

# tuplas = (1,2,3,4,5) # tuplas - nekeičiama sekos struktūra, panaši į sąrašą, bet negalima keisti elementų
# sarasas = [1,2,3,4,5] # sarasas - keičiama sekos struktūra, galima keisti elementus

# print(tuplas[0]) # greitesnis
# print(sarasas[0]) # letesnis



# sarasas = [1,2,3,4,5] # sarasas - keičiama sekos struktūra, galima keisti elementus

# if 2 in sarasas: # tikrina ar elementas yra sarase
#     print("Yra") # Išvedamas tekstas "Yra"

# zodynas = {"Lietuva":"Vilnius", # Lietuva - raktas(key), Vilnius - reikšmė(value)
#             "Latvija":"Riga",
#             "Estija":"Talinas",
#             "Lenkija":"Varšuva",
#             "Vokietija":"Berlynas",
#             "Prancūzija":"Paryžius"}

# if "Lietuva" in zodynas: # tikrina ar raktas yra zodyne
#     print("Yra") # Išvedamas tekstas "Yra"

# is
# sarasas = [1,2,3,4,5] 
# sarasas2 = [1,2,3,4,5] 

# if sarasas is sarasas:
#     print("Yra") # Išvedamas tekstas "Yra"

# if not 3> 5: # not paneigia (arba invertuoja) sąlygą
#     print("3 didesnis uz 5")

# dirbu dirbu...

# if 2> 3:
#     pass # nieko nedaro, bet leidžia tęsti kodą

# print("Baigta") # Išvedamas tekstas "Baigta"
# kintamasis = "labas" # kintamasis su tekstu
# if type(kintamasis) == str: # tikrina ar tipas yra int
#     print(type(kintamasis)) # Išvedamas tekstas "Yra"


# import time # tai ikelia kazkieno kito koda

# start_time = time.perf_counter() # pradeda matuoti laiką

# # cia rasomas kodas, kurio vykdymo laikas bus matuojamas

# # ilgai trunkanti opercija


# end_time = time.perf_counter() # baigia matuoti laiką

# print(f"Vykdymo laikas: {end_time - start_time} sek") # Išvedamas vykdymo laikas


# sakinys = "Sveiki studentai, tikiuosi, kad jums sekasi gerai" # o jeigu naudotojas iveda kitoki sakini ?

# sarasas = sakinys.split() 
# print(sarasas)
# trecias_zodis = sarasas[-3] # trecias_zodis = "jums"
# print(trecias_zodis[2])

sakinys = "Sveiki studentai, tikiuosi, kad jums sekasi gerai" # o jeigu naudotojas iveda kitoki sakini ?

sarasas = sakinys.split() 
print(sarasas)
print(sarasas[-3][2])

# trecias_zodis = "jums"

# print(trecias_zodis[2])
#
#
print("kito zmogaus pakeitimas")
