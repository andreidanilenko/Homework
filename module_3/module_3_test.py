# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(4))


print(round((max(len("hi"), len("world")) + min(len("hi"), len("world"))) / 2, 2))


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(isinstance(a, list)) # True
print(a == b) # True
print(a is b) # ???
print(a is c) # ???



# x = 10
# def foo():
#     x = 20
#     print(x)
# foo()
# print(x)
#
#
# def foo(n):
#     count = 0
#     for i in range(n):
#         if i % 3 == 0:
#             count += 1
#     return count
# print(foo(20))


def foo(n):
    if n == 0:
        return 1
    else:
        return n * foo(n - 1)


print(foo(4))
