import sqlite3
import random

if __name__ == '__main__':
    db = sqlite3.connect("dz7")
    courser = db.cursor()

    courser.execute('''CREATE TABLE IF NOT EXISTS namber
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    test_nambers INT)''')

    courser.execute('''CREATE TABLE IF NOT EXISTS text
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        test_text TEXT)''')
    db.commit()


    lst = input("Введите строку для иследования:\n").split()
    print(lst)

    for item in lst:
        try:
            if int(item) % 2 == 0:
                courser.execute('''INSERT INTO namber(test_nambers)
                                    VALUES (?)''', (item,))
                db.commit()
            elif int(item) % 2 != 0:
                courser.execute('''INSERT INTO text(test_text)
                                     VALUES ("нечетное")''')
                db.commit()

        except (ValueError):
            courser.execute('''INSERT INTO text(test_text)
                                            VALUES (?)''', (item,))
            courser.execute('''INSERT INTO namber(test_nambers)
                                            VALUES (?)''', (len(item),))
            db.commit()


    courser.execute('''SELECT * FROM namber''')
    a = courser.fetchall()
    print(a)
    courser.execute('''SELECT * FROM text''')
    a = courser.fetchall()
    print(a)
