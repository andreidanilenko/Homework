# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')


# a = [1, 1, 1]
# b = ''
# d = [1, 1, 1]
# c = d
# c[0] = 2
# print(c)
# print(d)
# print(id(a))
# print(id(d))
# print(id(c))
# print(c is d)
#
#
# def helper():
#     """
#     Эта функция-помощник
#     """
#     pass
#
# print(helper.__doc__)