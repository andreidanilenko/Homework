my_dict={'Андрей':1964, 'Ирина':1965,'Артём': 1991, 'Анна': 1995}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Андрей'])
print(my_dict.get('Денис','Not existing value: None',))
my_dict.update({'Денис': 1987, 'Сергей':1964})
print('Modified dictionary: ',my_dict)
a=my_dict.pop('Денис')
print('Deleted value: ',a)
print(my_dict)

my_set={1,2,3,2,2,2,True,True,'Андрей','Андрей',(7,8,9)}
print('Set: ',set(my_set))
my_set.add(5)
my_set.add('Kamila')
my_set.remove(1)
print('Modified set: ',my_set)

# phone_book={'Denis': 88005553535, 'Max': 88005553534}
# print(phone_book)
# #Ошибка если Денис в квадратные скобки phone_book={['Denis']: 88005553535, 'Max': 88005553534}
# print(phone_book['Denis'])
# phone_book['Denis']=1513489346
# print(phone_book)
# print(phone_book['Denis'])
# phone_book['Anton']=88005553533
# print(phone_book)
# del(phone_book['Max'])
# print(phone_book)
# phone_book.update({'Sasha':88005553532,'Alex': 88005553531})
# print(phone_book)
# print (phone_book.get ('Denis'))
# print (phone_book.get ('Kamila'))
# print (phone_book.get ('Kamila', 'Такого ключа нет'))
# a=phone_book.pop('Anton')
# print(a)
# print(phone_book)
# list_=[1,2,3]
# list_.pop(0)
# print(list_)
# print(phone_book)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())
# phone_book={'Denis': [88005553535, 204324], 'Max': 88005553534}
# print(phone_book)
# set_={1,2,3,4,5,1,2,3,4,'String',False,(1,2,3)}# Логическое значение в множестве не выводится на печать, если есть символы "1"=True или "0"=False
# print(set_)
# list_=[1,1,1,2,2,2,3,4]
# print(set(list_))
# list_=set(list_)
# print(list_) # print(list_[0]) ,извлекать по индексу будет ошибка, так как это множество
# print(list_.discard(1))
# print(list_)
# print(list_.remove(3))
# print(list_)
# list_.add(5)
# print(list_)
#
# name=input('Введите имя: ')
# print (phone_book.get (name, 'Такого ключа нет'))
