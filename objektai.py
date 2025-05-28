# class Dog(): # Klase - kaip sablonas
#     def __init__(self): # kai kuriam objekta, automastikai kreipiasi i sita
#         self.legs = 4 # legs - savybe


# suo = Dog() # sukuriamas objektas (inicilizuojamas objektas) kaip konkretus individas

# print(suo.legs)

# class Dog(): # Klase - kaip sablonas
#     def __init__(self, spalva): # Konstruktorius (__init__)
#         self.legs = 4 # legs - savybe
#         self.color = spalva

#     def bark(self, sound):
#         print(f"{self.color} dog says AU AU {sound}")


# reksas = Dog("Brown") # is esmes tarsi kviecaiams __init__

# print(reksas.legs, reksas.color)

# reksas.bark("GRRR")

# rikis = Dog("Black") # is esmes tarsi kviecaiams __init__

# print(rikis.legs, rikis.color)
# rikis.bark(" umm umm")

# class Human():
#     def __init__(self, ugis, weight, name, last_name):
#         self.arms = 2
#         self.legs = 2
#         self.head = 1
#         self.height = ugis
#         self.weight = weight
#         self.name = name
#         self.last_name = last_name

#     def bmi(self):
#         return self.weight / (self.height / 100) ** 2
    
#     def __str__(self): # kai meginam spausdinti automatiskai yra ieskoma str metodo
#         return f"{self.name} {self.last_name} kurio ugis yra {self.height} ir svoris yra {self.weight}"

# zmogus = Human(190,80, "Jonas", "Jonaitis")
# # print(zmogus.bmi())

# # zmogus2 = Human(int(input("Iveskite savo ugi (CM)")), int(input("Iveskite savo svori (kg)")))
# # print(f"Jusu KMI yra: {zmogus2.bmi()}")

# # print(zmogus)

# zmogus2 = Human(170,65, "Mantas", "Mantaitis")
# # print(zmogus2)


# zmones = [zmogus2]
# zmones.append(zmogus)

# for zm in zmones:
#     print(zm)
#     print(zm.bmi())

# import pickle

# with open('zmones.pickle',"wb") as failas:
#     pickle.dump(zmones,failas)
# import pickle
# with open('zmones.pickle',"rb") as failas:
#     zmones_nuskaitytas = pickle.load(failas)


# for zm in zmones_nuskaitytas:
#     print(zm)
#     print(zm.bmi())


# sarasas = [7,9,5,1,5]
# print(sarasas)

# print(list(range(5)))
# # print(list(range())) # Klaida
# print(list(range(2,5))) 
# print(list(range(2,20,3))) 
# sarasas = [2, 5, 8, 11, 14, 17]


# kiekis = 0

# for i in range(2,20,3): # i = 2 | i = 5 | i = 8 | i = 11 | i = 14 | i = 17
#     print(i) # print(2) | print(5) | print(8)
#     kiekis = kiekis + 1

# print(f"Kiekis {kiekis}")



# kiekis = 0

# for i in range(6): 
#     print(i) 
#     kiekis = kiekis + 1

# print(f"Kiekis {kiekis}")


# skaicius = 9
# print(skaicius)
# skaicius = 15
# print(skaicius)

# pazymiai = []
# for sk in pazymiai:
#     print(sk)


# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} is speaking")

#     def grazink_skaiciu(self):
#         return 5


# suo1 = Dog("Reksas")

# suo2 = Dog("Margis")

# suo1.speak()

# suo2.speak()

# print(suo1.grazink_skaiciu())
# import numpy as np
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x.T.shape)




# sarasas = [1,2,3]

# def spausdinti():
#     print(sarasas)

# spausdinti()

# sarasas_naujas = sarasas.copy()
# sarasas = [4,5,6]

# spausdinti()

# sarasas = [1,2,3]

# def spausdinti():
#     print(sarasas)

# spausdinti()

# sarasas.append(5)

# spausdinti()



# class Dog():
#     def __init__(self):
#         self.__kojos = 4 # __ pries kintamaji reiskia, kad jis yra privatus (pasiekiamas tik klases viduje)

#     def keisti_kojas(self, kojos):
#         if kojos >= 0 and kojos < 6:
#             self.__kojos = kojos


#     def _spausdinti_kojas(self):
#         print(self.__kojos)
#     def __str__(self): # str skirtas atvaizduoti daugiau, kai mus domina konkretus objektas tarsi duok informacija apie objekta
#         return f" str metodas {self.__kojos}"
#     def __repr__(self): # repr skirtas atvaizduoti "Bare minimum", kai mus domina tik supratimas apie kokia objekta eina kalba, bet detales nedomina. Nuo zodzio Represent. 
#         return f" repr metodas {self.__kojos}" 

# suo1 = Dog()
# suo2 = Dog()

# # # print(suo1.__kojos)
# # # suo1.__kojos = 3
# # # print(suo1.kojos)
# # suo1.keisti_kojas(3)
# # suo1._spausdinti_kojas()
# # # suo1.__vidinis()
# # # print(suo2.kojos)

# # # suo1.naujas = 9 # retai naudojama ganetinai unikali python savybe
# # # print(suo1.naujas)


# # suo1.begti() # printina as begu
# # suo1.begti() # pasitikrina kiek turi koju ir tada printina as begu su tam tikru kiekiu koju
# # stringas = str("Blablabla")
# # stringas.

# sunys = [suo1,suo2]

# # print(sunys) # kai printinam objektu sarasa naudojamas __repr__

# for suo in sunys:
#     print(suo) # kai printinam viena objekta, su print, tuomet naudojamas __str__

# # class Cat():
# #     pass

# # sunys.append(Cat())

# # for suo in sunys:
# #     if type(suo) is Dog:
# #         suo._spausdinti_kojas()

