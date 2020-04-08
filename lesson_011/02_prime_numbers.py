# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.number = 0
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        while self.number < self.n:
            if self.calculate_prime_number():
                self.prime_numbers.append(self.number)
                return self.number
        else:
            raise StopIteration()

    def calculate_prime_number(self):
        self.number += 1
        for prime in self.prime_numbers:
            if self.number % prime == 0:
                return False
        return True


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)


def main_filter_function(prime_number):
    prime_number = str(prime_number)
    count_prime_number = len(prime_number)
    if len(prime_number) >= 2:
        count_number = int(count_prime_number / 2)
        odd_char = 0 if len(prime_number) % 2 == 0 else 1
        ln = lucky_number(prime_number, count_prime_number, count_number, odd_char)
        p = palindrome(prime_number)
        t = trimorphic(prime_number, count_prime_number)
        print(f'Простое число: {prime_number} - {ln}, {p}, {t}')


def lucky_number(prime_number, count_prime_number, count_number, odd_char):
    first_syllable = prime_number[:count_prime_number - count_number - odd_char]
    last_syllable = prime_number[count_prime_number - count_number:]
    first_syllable = sum([int(x) for x in first_syllable])
    last_syllable = sum([int(y) for y in last_syllable])
    if first_syllable == last_syllable:
        return f'Счастливое'
    else:
        return f'Не счастливое'


def palindrome(prime_number):
    palindrome_number = prime_number[::-1]
    if int(prime_number) == int(palindrome_number):
        return f'Палиндромное'
    else:
        return f'Не палиндромное'


def trimorphic(prime_number, count_prime_number):
    """
    Триморфное число — натуральное число, десятичная запись куба которого оканчивается цифрами самого этого числа.
    https://ru.wikipedia.org/wiki/Триморфное_число
    """
    prime_number = int(prime_number)
    trimorphic_number = str(prime_number ** 3)
    trim_num_syllable = int(trimorphic_number[-count_prime_number:])
    if prime_number == trim_num_syllable:
        return f'Триморфное'
    else:
        return f'Не триморфное'


for number in prime_numbers_generator(n=10000):
    main_filter_function(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

# зачет!
