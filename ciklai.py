# sarasas = [4,5,1,7,2,9]

# # for # pagrindinis ciklo zodis

# for skaicius in sarasas: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = sarasas[0] | 2 iteracija - skaicius = sarasas[1] | 3 iteracija - skaicius = sarasas[2] | 4 iteracija - skaicius = sarasas[3] | 5 iteracija - skaicius = sarasas[4] | 6 iteracija - skaicius = sarasas[5]
#     print(skaicius) # isveda kiekviena skaiciu is saraso
#     print("Skaicius atspausdintas")


# zodziai = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"] # sarasas su zodziais

# for zodis in zodziai:
#     print(zodis)

# skaiciai = [7,4,9,2,4,3,1,5,6,8] # sarasas su skaiciais

# suma = 0

# for skaicius in skaiciai: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = skaiciai[0] | 2 iteracija - skaicius = skaiciai[1] | 3 iteracija - skaicius = skaiciai[2] | 4 iteracija - skaicius = skaiciai[3] | 5 iteracija - skaicius = skaiciai[4] | 6 iteracija - skaicius = skaiciai[5]
#     suma = skaicius + suma
#     print(f"Tarpine suma: {suma}") 

# print(suma)

# sudeti visus lyginius skaicius is saraso
# skaiciai = [7,4,9,2,4,3,1,5,6,8] # sarasas su skaiciais
# suma = 0

# for skaicius in skaiciai: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  skaicius = skaiciai[0] | 2 iteracija - skaicius = skaiciai[1] | 3 iteracija - skaicius = skaiciai[2] | 4 iteracija - skaicius = skaiciai[3] | 5 iteracija - skaicius = skaiciai[4] | 6 iteracija - skaicius = skaiciai[5]
#     if skaicius % 2 == 0: # tikriname ar skaicius lyginis
#         suma = suma + skaicius # jei lyginis, sudedame prie sumos
#         print(f"Tarpine suma: {suma}")

# print(f"Galutine suma: {suma}") # isvedame galutine suma


# sarasas = [4, 'Labas', 8.5, True, 7] # sarasas su ivairiais elementais

# for mano_kintamasis in sarasas: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  mano_kintamasis = sarasas[0] | 2 iteracija - mano_kintamasis = sarasas[1] | 3 iteracija - mano_kintamasis = sarasas[2] | 4 iteracija - mano_kintamasis = sarasas[3] | 5 iteracija - mano_kintamasis = sarasas[4]
#     print(mano_kintamasis) # isveda kiekviena elementa is saraso

# sarasas_sarase = [4,5,2,4,8,[9,2,1],7,4,[5,4,2]] # sarasai gali turėti sarasus

# # print(sarasas_sarase) # isveda sarasa su sarasu

# print(sarasas_sarase[5][0]) 

# zodynas = {"Ugne":[9,8,10,9,10], "Mantas":[8,9,10,9,10], "Tomas":[7,8,9,8,9]} # zodynas su sarasais
# # print(zodynas) # isveda zodyna


# suma = 0

# for elementas in zodynas["Ugne"]: # for ciklas, kuris iteruoja per sarasa | 1 iteracija -  elementas = zodynas["Ugne"][0] | 2 iteracija - elementas = zodynas["Ugne"][1] | 3 iteracija - elementas = zodynas["Ugne"][2] | 4 iteracija - elementas = zodynas["Ugne"][3] | 5 iteracija - elementas = zodynas["Ugne"][4]
#     suma += elementas # sudedame visus elementus
#     print(suma) # isveda tarpine suma

# print(suma/len(zodynas["Ugne"])) 

# amziai = {"Ugne": 32, "Mindaugas":30, "Justas":26}

# print(amziai)

# print(amziai.keys())

# for key in amziai.keys(): # keys eina per raktus
#     print(key) # isveda visus zodyno raktus


# amziai = {"Ugne": 32, "Mindaugas":30, "Justas":26}

# print(amziai)

# print(amziai.values())

# for value in amziai.values(): # values eina per reiksmes
#     print(value) # isveda visus zodyno raktus

# range - leidzia nustatyti kiek kartu bus kartojamas ciklas

# range is esmes tiesiog sukuria sarasa su skaiciais nuo 0 iki n-1 | range(5) - [0,1,2,3,4] | range(5,10) - [5,6,7,8,9] | range(5,10,2) - [5,7,9] | range(10,5,-1) - [10,9,8,7,6] | range(0,-10,-1) - [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]

# for i in range(5): # range(5) - [0,1,2,3,4] | 5 kartus
#     print(i) # isveda 0,1,2,3,4



# for i in range(3,8): # range turi panasia sintakse kaip ir slicing range(start,stop,step) | jeigu tik vienas skaicius - tai bus stop | jeigu du - tai bus start ir stop | jeigu trys - tai bus start, stop ir step
#     print(i)

# for i in range(3,8,2): # range turi panasia sintakse kaip ir slicing range(start,stop,step) | jeigu tik vienas skaicius - tai bus stop | jeigu du - tai bus start ir stop | jeigu trys - tai bus start, stop ir step
#     print(i)

# range(5) # [0,1,2,3,4] 
# [0,1,2,3,4]

# sarasas = [0,1,2,3,4]

# for skaicius in range(5):
#     print("Labas")

# kiekis = int(input("Iveskite skaiciu:"))

# for i in range(kiekis): # range(7) - [0,1,2,3,4,5,6,7] | i = 0 | i = 1
#     input("Iveskite zodi:") # laukia kol bus ivestas zodis

# tekstas = "Lauke lyja"
# simbolis = 'L'
# for raide in tekstas: # raide = tekstas[0] | raide = tekstas[1]
#     print(raide)



# print("L")
# print("a")
# print("u")
# print("k")
# print("e")
# print(" ")
# print("l")
# print("y")
# print("j")
# print("a")


# vardai_pavardes = {'Ugne': 'Urbonaite', 'Mantas': 'Miknevičius', 'Tomas': 'Tamošaitis', 'Justas': 'Jankauskas', 'Mindaugas': 'Miknevičius'}

# vardas = input("Iveskite varda")

# for kvp in vardai_pavardes.items():
#     if kvp[0] == vardas:
#         print(f"Sveiki {kvp}") # isveda visus zodyno elementus


# fraze = input("Iveskite fraze: ") # laukia kol bus ivestas zodis
# atbulinis = ''
# for indeksas in range(len(fraze)-1,-1,-1):
#     atbulinis += fraze[indeksas] # sudedame atbuline fraze
# print(f"Jusu ivestas zodis {fraze} apsukus yra {atbulinis}")


