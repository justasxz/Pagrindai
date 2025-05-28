import os
import datetime
# print(dir(os))

# print(os.getcwd()) # current working directory

# os.chdir("D:\AIU7") # change directory

# print(os.getcwd()) # current working directory

# print(os.listdir()) # list files in directory

# os.mkdir("aplankas\Mano_direktorija") # create directory

# os.makedirs(r"D:\AIU7\Pagrindai\Mano_direktorija\Mano\Tavo\Gera") # create directory

# svarbus pastebejimas
# jeigu nurodome visa kelia nuo disko pvz C:, D: tai mums nesvarbu kokiam aplanke esame
# jeigu nurodome kelia tik iki aplanko pvz aplankas\Mano_direktorija tai jis sukurs aplanka tik tame aplanke kuriame esame
# os.chdir("D:\AIU7") # change directory

# sukurimas = os.stat("Pagrindai").st_birthtime # get directory status

# print(datetime.datetime.fromtimestamp(sukurimas)) # convert to datetime
# dabar = datetime.datetime.now()
# dabar.timestamp() # get current timestamp

# failas = open("failas.txt", "w")
# failas.write("Labas rytas\n")
# input("Paspauskite bet kuri klavišą, kad uždarytumėte failą...") # wait for user input
# failas.close() # close file
# input("Failas uždarytas. Paspauskite bet kuri klavišą, kad tęstumėte...") # wait for user input
# with open("failas.txt", "w") as failas: # w - rasyti (write), r - skaityti (read), a - prideti (append) | failas = open("failas.txt", "w")
#     failas.write("Labas rytas\n")
#     failas.write("Labas vakaras\n")

# failas.write("Labas vakaras\n") # klaida, nes failas jau uzdarytas
# galima isivaizduoti, kad failas.close() yra automatinis

# with open("failas.txt", "w") as failas: # w - sukuria faila jeigu jo nera, jeigu yra tai jis ji perraso
#     failas.write("Mano uzrasai\n")
#     failas.write("Labas rytas\n")
#     # failas.read() # klaida, nes failas rasymo rezimu

# with open("failas.txt", "r") as failas: # r - skaito faila jeigu failo nera tai klaida
    # tekstas = failas.read() # read file
    # print(tekstas) # spausdina failo turini
    # print(failas.readline()) # read line by line
    # read line by line with loop with readline()
    # while True:
    #     line = failas.readline()
    #     if not line:
    #         break
    #     print(line.strip()) # remove new line character

    # print(failas.readlines()) # read all lines
    # failas.write("Labas rytas\n") # klaida, nes failas skaitymo rezimu

# with open("failas.txt", "a") as failas: # a - prideda prie failo, jeigu failo nera tai jis ji sukuria
    
#     failas.write("Labas vakaras\n")
#     failas.write("Labas naktis\n")

# with open("failas.txt", "r+") as failas: # r+ - skaito ir raso faila, jeigu failo nera, tai klaida
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini

# with open("failas.txt", "w+") as failas: # w+ - sukuria faila jeigu jo nera, jeigu yra tai jis ji perraso ir skaito faila
#     failas.write("Labas rytas\n")
#     failas.seek(0)
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini



# with open("failas.txt", "w", encoding="utf-8") as failas:
#     failas.write("Kęstutis") # K ę - o tai kaip man irasyti sita savo nesamoninga simboli ?
#     failas.write("ė")

# with open("failas.txt", "r", encoding="utf-8") as failas:
#     tekstas = failas.read() # read file
#     print(tekstas) # spausdina failo turini
     

import pickle

# with open("duomenys.pickle", "wb") as failiukas: # wb - binary write
#     pickle.dump("Labas rytas", failiukas) # write to file

# with open("duomenys.pickle", "rb") as failiukas: # rb - binary read
#     tekstas = pickle.load(failiukas) # read from file
#     print(tekstas) # spausdina failo turini
# sarasas = [5,4,19,2,6,48,1,0,3,7,8,9,10]
# sarasas.append(5)
# with open("duomenys.txt", "w") as failiukas: # w - write
#     failiukas.write(str(sarasas)) # write to file

# with open("duomenys.txt", "r") as failiukas: # r - read
#     tekstas = failiukas.read() # read from file
#     print(tekstas) # spausdina failo turini

# sarasas = [5,4,19,2,6,48,1,0,3,7,8,9,10]
# with open("duomenys.pickle", "wb") as failiukas: # wb - binary write
#     pickle.dump(sarasas, failiukas) # write to file

# with open("duomenys.pickle", "rb") as failiukas: # rb - binary read
#     nuskaitytas_sarasas = pickle.load(failiukas) # read from file
#     nuskaitytas_sarasas.append(5) # prideti elementa i sarasa
#     print(nuskaitytas_sarasas) # spausdina failo turini

# saras_sarase = [[1,2,3],[4,5,6],[7,8,9]]
# zodynai_sarase = [{"vardas":"Jonas","pavarde":"Jonaitis"},{"vardas":"Petras","pavarde":"Petraitis"},{"vardas":"Ona","pavarde":"Onaitė"}]
# print(zodynai_sarase)