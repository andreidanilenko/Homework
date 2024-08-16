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