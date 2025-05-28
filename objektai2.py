# class Vehicle():
#     def __init__(self, speed, material):
#         self.speed = speed
#         self.material = material
#     def __str__(self):
#         return f"Made from {self.material} and speed of {self.speed}"


# class LandVehicle(Vehicle):
#     def __init__(self, speed, material, wheels):
#         super().__init__(speed, material) # Vehicle.__init__
#         self.wheels = wheels

#     def __str__(self):
#         return super().__str__() + f" and with {self.wheels} wheels"
    
#     def vaziuoti(self):
#         print(f"As vaziuoju {self.wheels} ratais")

# class WaterVehicle(Vehicle):
#     pass



# class AirVehicle(Vehicle):
#     pass

# tr_pr = Vehicle(30,"Aluminium")
# saus_tr_pr = LandVehicle(180,"Aluminium",4)
# vand_tr_pr = WaterVehicle(30,"Aluminium")

# print(tr_pr)
# print(saus_tr_pr)
# print(vand_tr_pr)


# # tr_pr.vaziuoti()
# saus_tr_pr.vaziuoti()
# # vand_tr_pr.vaziuoti()


class Gyvunas():
    def __init__(self, age, color, vardas):
        self.age = age
        self.colour = color
        self.name = vardas

    def kalbeti(self):
        print("As kalbu kaip moku")

    def __str__(self): # Kai mes darom pvz print(gyvuno_objektas), jis skirtas duoti detalia informacija apie viena objekta
        return f"Labas as {self.name} man {self.age} ir mano spalva yra {self.colour}"
    
    def __repr__(self): # kai mes darome print(guvunu_sarasas), jis skirtas trumpai reprezentuoti gyvuna sarase
        return self.name


class Dog(Gyvunas):
    def __init__(self, age, color, vardas):
        super().__init__(age, color, vardas)

    def kalbeti(self):
        print("As esu suo ir loju AU AU")

class Cat(Gyvunas):
    def __init__(self, age, color, vardas):
        super().__init__(age, color, vardas)

suo = Dog(7,"Ruda","Reksas")
suo2 = Dog(1,"Balta","Mikis")

kate = Cat(2,"Orandzine","Maja")
kate2 = Cat(3,"Juoda","Mice")

gyvunai = [suo,suo2,kate,kate2]

print(gyvunai)

for gyvunas in gyvunai:
    print(gyvunas)
    gyvunas.kalbeti()