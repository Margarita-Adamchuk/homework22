# тренировка
def moon_weidht(weidht, weight_gain, age):
    print(f"Расчитаем ваш вес на луне через {age} лет, при условии что вы прибовляете по {weight_gain}кг в год.")
    weidht = weidht * 0.165
    weight_gain = weight_gain * 0.165
    age = age
    for result in range(1, age + 1):
        weidht = weidht + weight_gain
        print(f"Год {result}: ваш вес {weidht}")

moon_weidht(65, 2, 6)