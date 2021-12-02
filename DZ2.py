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
        print("'Лошадь мчиься пверед!'")

class Jockey:

    def __init__(self, name_jockey, neme_horse):
        self.name_jockey = name_jockey
        self.name_horse = neme_horse

    def ride(self):
        print(f"Ну что {self.name_jockey} поехали котаться!!!")
        Horse.hop(self.name_horse)

if __name__ == '__main__':
    hari = Jockey("ГАРИ", "Розачка")
    rozi = Horse("Розачка", "Белая", "Пони")

    hari.ride()

