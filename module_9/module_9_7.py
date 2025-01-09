def is_prime(func):
    def checked_number(*args):
        result = func(*args)
        if result < 2:
            return
        if result in (2, 3):
            print("Простое")
            return result
        if result % 2 == 0 or result % 3 == 0:
            print("Составное")
            return result
        i = 5
        while i * i <= result:
            if result % i == 0 or result % (i + 2) == 0:
                print("Составное")
                return result
            i += 6
        print("Простое")
        return result
    return checked_number

@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res

result = sum_three(2, 3, 6)
print(result)


# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three