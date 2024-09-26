first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('Введите третье число: '))
if first==second==third:
     print ("Количество одинаковых чисел: ",3)
elif first==second or first==third or second==third:
     print("Количество одинаковых чисел: ",2)
else:
#elif first!=second or first!=third or second!=third:
     print("Количество одинаковых чисел: ", 0)

# number=int(input('Введите число: '))
# if number%3==0 and number%5==0:
#     print('FizzBuzz')
# elif number%3==0:
#     print('Fizz')
# elif number%5==0:
#         print('Buzz')
# else:
#     print('Число не подходит')