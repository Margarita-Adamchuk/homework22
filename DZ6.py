# Создать класс Medical_Center

class Medical_Center:
    counter = 0
    database_name = []
    database_age = []
    database_doktor = []

    def __init__(self, name):
        self.name = name
        print(f"{self.name} дабро пожалавать в наш медецинский центр!")
        self.age = int(input("Сколько вам лет: "))
        self.doktor = input("К какому врачу вы идете: ")
        self.namber = 0
        Medical_Center.counter += 1
        Medical_Center.database_name.append(self.name)
        Medical_Center.database_age.append(self.age)
        Medical_Center.database_doktor.append(self.doktor)

    def age_determination_max(self):
        print("Возраст самого старшего поселителя:")
        return max(Medical_Center.database_age)

    def age_determination_min(self):
        print("Возраст самого молодого поселителя:")
        return min(Medical_Center.database_age)

    def __str__(self):
        print("Информация о всех поситителях")
        for item in range(len(Medical_Center.database_name) - 1):
            print("_____________________________________")
            print(f"| {item} | {Medical_Center.database_name[self.namber]} |"
                  f" {Medical_Center.database_age[self.namber]} | "
                  f"{Medical_Center.database_doktor[self.namber]}")
            print("______________________________________")
            self.namber =+ 1

a = list()