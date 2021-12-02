# Создать класс с информацией о почтовом адресе

class Post:

    def __init__(self, name, siti, adress, index):
        self.name = name
        self.siti = siti
        self.adress = adress
        try:
            self.index = int(index)
        except ValueError:
            print("ОШИБКА ВВОДА!!!Индекс должен содержать только цифры!!!")

    def new_name(self):
        print("Вы хотите изменить имя получателя. Введите новое имя")
        self.name = input()

    def new_siti(self):
        print("Вы хотите изменить город. Введите новый город")
        self.siti = input()

    def new_adress(self):
        print("Вы хотите изменить адрес. Введите новый адрес")
        self.name = input()

    def new_index(self):
        print("Вы хотите изменить индекс. Введите новый индекс")
        try:
            self.index = int(input())
        except ValueError:
            print("ОШИБКА ВВОДА!!!Индекс должен содержать только цифры!!!")

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.adress}\n" \
               f"{self.index} {self.siti}"



letter = Post(input("Имя: "), input("Город: "), input("Адрес: "), input("Индекс: "))
letter.new_name()
print(letter)

