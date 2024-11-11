info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            file.write(i + '\n')

    string_positions = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        str_num = 1
        while True:
            begin_cursor = file.tell()
            line = file.readline().rstrip('\n')

            if not line:
                break
            string_positions[(str_num, begin_cursor)] = line
            str_num += 1
    return string_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
