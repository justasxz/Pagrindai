# suma = 0
# for sk in sarasas:
#     suma = suma + sk

# min(sarasas) - duoda maziausia skaiciu is saraso
# max(sarasas) - duoda didziausia skaiciu is saraso
# sum(sarasas) - susumuoja saraso skaicius ir atiduoda viena rezultata
# mean(sarasas) sudeda visus skaicius ir padalina is kiekio (vidurkis)
# median(sarasas) - 
# from statistics import median
# sarasas = [6,1,10,8,9,2] # -> [1,2,6,8,9,10]
# print(median(sarasas))


# list comprehension - greitas saraso sudarymas

# sarasas = [7,5,4,2, 5 ,4, 8, 3, 11, 27, 30]

# # kvadratai = []

# # for sk in sarasas:
# #     kvadratai.append(sk**2)

# # print(kvadratai)

# kvadratai = [x**2 for x in sarasas]
# print(kvadratai)

# kvadratai = [x**2 for x in sarasas if x % 2 == 0]

# # for sk in sarasas:
#     #  if sk % 2 == 0
# #     kvadratai.append(sk**2)

# print(kvadratai)


sarasas = [5,1,9,45,6,1,6,4,1,5,7,91,23,1,6,43,20,6]

# sarasas.sort() # rikiuoja nuo maziausio iki didziausio
# print(sarasas)
# sarasas.sort(reverse=True) # rikiuoja nuo didziausio iki maziausio
# print(sarasas)

# sorted - privalumas nuo sort, nes sort - tinka tik sarasams, tai yra saraso specifinis metodas.
# sorted - tinka visom "Lentynom" (lentyn7 tipams)

# naujas = sorted(sarasas) 
# print(sarasas)
# print(naujas)

# tuplas = (4,7,65,16,8,7486,53)
# naujas_t = sorted(tuplas)
# print(naujas_t)

# zodynas = {"Mantas":20,"Karolis":23,"Jonas":15,"Antanas":22, "Zigmas":19}

# naujas = sorted(zodynas)
# print(zodynas)
# print(naujas)


# pagal_laika = sorted(zodynas.items(), key=lambda x: x[1]) # x = (Mantas,20) | x = (Karolis,23)
# print(pagal_laika)
# print(abs(-5))
# from operator import attrgetter
print("Daugiau triuku")