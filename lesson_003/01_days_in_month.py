# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1:
    print('В указанном месяце 31 день')
elif month == 2:
    print('В указанном месяце 28 дней')
elif month == 3:
    print('В указанном месяце 31 день')
elif month == 4:
    print('В указанном месяце 30 дней')
elif month == 5:
    print('В указанном месяце 31 день')
elif month == 6:
    print('В указанном месяце 30 дней')
elif month == 7:
    print('В указанном месяце 31 день')
elif month == 8:
    print('В указанном месяце 31 день')
elif month == 9:
    print('В указанном месяце 30 дней')
elif month == 10:
    print('В указанном месяце 31 день')
elif month == 11:
    print('В указанном месяце 30 дней')
elif month == 12:
    print('В указанном месяце 31 день')
else:
    print('Такого месяца не существует!!!')