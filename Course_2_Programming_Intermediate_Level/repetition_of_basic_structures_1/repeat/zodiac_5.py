# put your python code here
def year_of_the_animal(y):
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь",
               "Овца"]
    for i in range(12):
        if y % 12 == i:
            return animals[i]


year = int(input())

print(year_of_the_animal(year))