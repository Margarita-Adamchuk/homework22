# Класс описывающий работников: ФИО, стаж, часовая зороботная плата, количество отработанных часов

class Employee:

    def __init__(self, name):
        self.name = name
        self.experience = int(input("Введите стаж: "))
        self.mani = int(input("Введите з/п за час: "))
        self.time = int(input("количество отработанных часов: "))

    def wages(self):
        print(f"Вы отработали {self.time} часов. Выша заработная плата,"
              f"согласно вашего стажа {self.experience} лет, будет равна: ")
        if self.experience < 1:
            print(self.mani * self.time)
        elif 3 > self.experience >= 1:
            print(self.mani * self.time + (5 * self.mani * self.time / 100))
        elif 5 > self.experience >= 3:
            print(self.mani * self.time + (8 * self.mani * self.time / 100))
        else:
            print(self.mani * self.time + (15 * self.mani * self.time / 100))

    def __str__(self):
        return f"Имя сотрудника: {self.name}. Его стаж {self.experience} лет, " \
               f"Зароботная плата за 1 час будет равна {self.mani} рублей"

name1 = Employee("Adamchuk")
print(name1)
name1.wages()
