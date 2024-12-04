import os
import time
from datetime import datetime
from pathlib import Path

# Получаем список файлов в текущей директории
file = [f for f in os.listdir() if os.path.isfile(f)]

# Получаем статистику файла
file_stat = os.stat(file[1])

# Получаем время изменения файла (st_ctime)
filetime = file_stat.st_mtime

# Преобразуем время в объект datetime
dt_object = datetime.fromtimestamp(filetime)

# Форматируем время в нужный формат
formatted_time = dt_object.strftime("%d.%m.%Y %H:%M")

# Получаем размер файла
filesize = file_stat.st_size

# Получаем путь к файлу
filepath = Path(file[1]).absolute()

# Получаем родительскую директорию
parent_dir = filepath.parent

print(f'Обнаружен файл: {file[1]}, Путь: {filepath}, Размер: {filesize} байт, '
      f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Этот код решает проблему с форматированием времени изменения файла[1][2]. Вот что изменилось:
#
# 1. Мы используем file_stat.st_mtime для получения времени изменения файла[1][2].
# 2. Преобразуем это время в объект datetime с помощью datetime.fromtimestamp()[5].
# 3. Форматируем время в нужный формат с помощью strftime()[5].
#
# Также обратите внимание, что:
#
# - Мы используем Path(file[1]).absolute() для получения полного пути к файлу[3].
# - parent_dir теперь получается напрямую из объекта Path[3].
#
# Этот код должен корректно отображать информацию о файле, включая отформатированное время его изменения.