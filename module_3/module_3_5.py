
def get_multiplied_digits(number):
    str_number = str(number)

    if not str_number:
        return 1

    first = int(str_number[0])

    if len(str_number) > 1:
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return get_multiplied_digits(int(str_number[1:]))
    else:
            return first if first != 0 else 1


result = get_multiplied_digits(40203)
print(result)


# Самостоятельная работа по уроку "Рекурсия"
# Цель: применить знания о рекурсии в решении задачи.
#
# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
#
# Пункты задачи:
# Напишите функцию get_multiplied_digits и параметр number в ней.
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
#
# Пример результата выполнения программы:
# Исходный код:
# result = get_multiplied_digits(40203)
# print(result)
# Вывод на консоль:
# 24
#
# Примечания:
# При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
# Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка заключается в бесконечной рекурсии или же в неверном обращении по индексу.


# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
#
# print(summa(5))


# def recursion():
#     recursion()
#
# recursion()


# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)