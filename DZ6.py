# Создать класс Medical_Center
import sqlite3

class Medical_Center:
    counter = 0
    db1 = sqlite3.connect("Visitors")
    courser = db1.cursor()

    courser.execute('''CREATE TABLE IF NOT EXISTS table1
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT,
                            Age INT,
                            Doctor TEXT)''')

    db1.commit()

    def __init__(self, name):
        self.name = name
        self.age = int(input("Сколько вам лет: "))
        self.doctor = input("К какому врачу вы идете: ")
        Medical_Center.counter += 1
        Medical_Center.courser.execute('''INSERT INTO table1(Name, Age, Doctor)
                                      VALUES (?, ?, ?)''', (self.name, self.age, self.doctor))
        Medical_Center.db1.commit()


if __name__ == '__main__':
    print("Дабро пожаловать в наш медецинский центр!")
    visitors1 = Medical_Center(input("Каквас зовут"))
    Medical_Center.courser.execute('''SELECT * FROM table1''')

    print(Medical_Center.courser.fetchall())
