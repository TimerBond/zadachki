d = {"Понедельник": True,
     "Вторник": True,
     "Среда": True,
     "Четверг": True,
     "Пятница": True,
     "Суббота": False,
     "Воскресенье": False}
i = 1
for key, value in d.items():
    print(str(i) + ":", key, end=" - ")
    if value:
        print("рабочий день")
    else:
        print("выходной день")
    i += 1
