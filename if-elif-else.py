# Условные операторы

x = 7
if x == 7:                 #если х равен 7 то ты прав
     print("Ты прав")
else:                      #иначе надо сделать и что вывести
     print("НЕТ")

print("---------------------------------------------------------------------------------------------------------------")

age = 2
if (age <= 3):                       #если --> иначе если -->иначе если -->иначе
    print("ТЫ ребенок")
elif (age >= 4) and (age <=14):
    print("Ты подросток")
elif (age >= 15) and (age <=30):
    print("Ты юноша")
else:
    print("Ты взрослый")

print("---------------------------------------------------------------------------------------------------------------")

all_cars = ['chrusler',  'dacia' ,'bmw', 'Kia' , 'vw' ,'seat', 'skoda' , 'lada', 'audi' , 'ford' , ' Chevrolet' ]
german_cars = ['bmw', 'vw' , 'audi']

if "lada" in all_cars:
    print("Да, я просмотрел все машины в массиве all_cars и нашел lada")    #так я проверил, есть lada в массиве и вывел результат
else:
    print("Я ничего не нашел")

print("----------------------------------------------------------------------------------------------------------")

for x in all_cars:
  if x in german_cars:
      print(x + " German_cars")         #Так я циклом просмотрел все машины из массива all_cars, а потом условным оператором сверил
  else:                                 #с другим циклом и вывел нужную мне инфу
      print(x + " NO German cars")

print( "------------------------------------------------------------------------------------------------------------")


