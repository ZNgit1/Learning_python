enemy = {
    'loc_x': 50,
    "loc_y": 70,
    "color": "green",                               #мой словарь
    "helth": 100,
    "name": "furik"
}

print(enemy)
print("loc_x:" + str(enemy["loc_x"]))           #при работе с числами используются str
print("loc_y:" + str(enemy["loc_y"]))

enemy['rang'] = 'Admiral'      # добавил в словарь единицу
print(enemy)

del enemy ["color"]   #удалил из словаря единицу
print(enemy)

enemy["loc_x"] = enemy["loc_x"] + 30     #провел математическое действие
print(enemy)

if enemy["helth"] < 1100:           #если здоровье меньше 1100 то цвет меняем на red
    enemy ["color"] = "red"

print(enemy)

print(enemy.values())     #словарь делится на keys И values
print(enemy.keys())

