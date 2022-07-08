"""Поиск любых файлов на компьютере."""
import os, shutil

KEY_FOR_SEARCH = input('Что ищем???\n')

def search():
    for adress, dirs, files in os.walk(input('Введите путь старта\n')):
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(adress, file)

def read_from_pathtxt(path):
    with open(path) as r:
        for i in r:
            if KEY_FOR_SEARCH in i:
                return path                

for i in search():
    read_from_pathtxt()
