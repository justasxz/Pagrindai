
# bool tipo kintamasis
# bool_tipo = 5==5 # = - priskiria | == klausia ar lygu

# print(bool_tipo)

# bool_tipo = 4>=5 # = - priskiria | == klausia ar lygu

# print(bool_tipo)

# bool_tipo = (4>=5) or (5 > 7 and 4 > 5) # = and reiskia abi salygos teisingos | or bent viena teisinga

# print(bool_tipo)

# if - salygos sakinys

# skaicius = int(input("Iveskite savo skaiciu: "))

# if skaicius > 1:  # po dvitaskio pythone visados eina atitrauktos eilutes
#     print("Labas") # atitrauktos eilutes yra vykdomos tik tada jeigu salyga yra teisinga
#     print("Tavo ivestas skaicius yra daugiau uz 1")
#     print("Labas")

# print("Programa baigta")


# amzius = int(input("Iveskite savo amziu: "))

# if amzius >= 18:
#     print("Gali nusipirkti energetini gerima")

# if amzius >= 20:
#     print("Gali nusipirkti ir salto gerimo")

# if amzius >= 65:
#     print("Tu esi pensininkas")

# amzius = int(input("Iveskite savo amziu: "))
# stazas = int(input("Iveskite savo staza (metais): "))

# if amzius >= 18:
#     print("Gali nusipirkti energetini gerima")

# if amzius >= 20:
#     print("Gali nusipirkti ir salto gerimo")

# if amzius >= 65:
#     print("Tu esi pensininkas")
#     if stazas > 10: # jeigu apgaubiantis ifas yra netiesa, vidinis yra net netikrinamas
#         print("jus gaunate pensija")
#     # print("Grizome i pirma ifa")


# amzius = int(input("Iveskite savo amziu: "))

# if amzius >= 65: # tikrinama ar tiesa
#     print("Tu esi pensininkas")
# else: # jeigu netiesa ivyksta else
#     print("Tu nesi pensininkas")



# if "LABAs".isupper():
#     print("visas tavo zodis yra didziosiomis raidemis")

# ivestis = input("Iveskite skaiciu: ")

# if ivestis.isdigit():
#     print("Aciu ivedete teisingai")
#     suma = 5 + int(ivestis) # tai dabar garantuoju sau, kad nebus klaidos ir visad teisingai paversime i int
# else:
#     print("ivedete arba ne skaiciu arba ne teigiama sveika skaiciu")

# vardas = "justas"
# if vardas == "Justas":
#     print("Sveiki Justai, as tave pazystu")
# else:
#     print("as tave nepazystu")


# amzius = int(input("Iveskite savo amziu: "))

# if amzius > 65: # sitas patikrinamas visada
#     print("Tu esi pensininkas")
#     if amzius > 80:
#         print("Dar kazkas")
# elif amzius > 20: # sitas tikrinamas tik jeigu pirmas yra netiesa
#     print("Gali nusipirkti ir salto gerimo")
# elif amzius > 18: # sitas tikrinamas tik jeigu pirmas ir antras yra netiesa
#     print("Tu gali nusipirkti energetini gerima")
# else: # jeigu visi trys netiesa
#     print("nezinau ka su tavimi daryti")



# if amzius > 65: # sitas patikrinamas visada
#     print("Tu esi pensininkas")

# if amzius > 20: # sitas patikrinamas visada
#     print("Gali nusipirkti ir salto gerimo")

# if amzius > 18: # sitas patikrinamas visada
#     print("Tu gali nusipirkti energetini gerima")
# else: # jeigu trecias if netiesa
#     print("nezinau ka su tavimi daryti")



# amzius = 20
# # skirtas tam, kai reikia palyginti daug salygu ar ji yra lygi kazkam 
# match amzius:
#     case 0: # if amzius == 0:
#         print("Tu katik gimei")
#     case 1 : # elif amzius == 1:
#         print("Tu esi kudikis")
#     case 10 : # elif amzius == 10:
#         print("Tu esi vaikas")
#     case 20 : # elif amzius == 20:
#         print("Tu esi jaunas suaugęs žmogus")
#     case _: # else:
#         print("Tu esi suaugęs žmogus")




