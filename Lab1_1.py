"""По номеру месяца напечатать пору года."""

x=int(input("Введите целое число от 1 до 12:\n"))

if x == 1:
   print("Январь")
elif x == 2:
   print("Февраль")
elif x == 3:
   print("Март")
elif x == 4:
   print("Апрель")
elif x == 5:
   print("Май")
elif x == 6:
    print("Июнь")
elif x == 7:
    print("Июль")
elif x == 8:
    print("Август")
elif x == 9:
    print("Сентябрь")
elif x == 10:
    print("Октябрь")
elif x == 11:
    print("Ноябрь")
elif x == 12:
    print("Декабрь")
else:
    print("Вы ввели неправильное число")
