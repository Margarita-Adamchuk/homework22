# Взаимодействие двух классов. Делала до перепросмотра уроков
class Horse:
    hooves = 4
    population = 0

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        Horse.population += 1

    def nicker(self):
        print("Иго-го, Иго-го, Иго-го")

    def hop(self):
        print(f"'{self.name} мчиься пверед!'")

class Jockey(Horse):

    def __init__(self, name_jockey, name, color, breed):
        Horse.__init__(self, name, color, breed)
        self.name_jockey = name_jockey


    def ride(self):
        print(f"Ну что {self.name_jockey} поехали котаться!!!")
        Horse.hop(self)

if __name__ == '__main__':

    hari = Jockey("ГАРИ", "Розочка", "серый", "пони")
    hari.ride()

