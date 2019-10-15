# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
full_expenses = expenses  # Можно это сразу здесь сделать
# Счётчик для цикла while
count = 0
expenses_sum = 0
while count < 9:
    # Расчёт 3% ежемесечно от стоимости
    x = (expenses * 3) / 100
    expenses += x
    expenses_sum += expenses
    count += 1
full_educational_grant = educational_grant * 10
full_expenses += expenses_sum
parent_money = round(full_expenses - full_educational_grant, 2)
print(f' Студенту надо попросить {parent_money} рублей')

# зачет!
