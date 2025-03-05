import re
import sys

def fix_phone(phone):
    phone = phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    if len(phone) == 11 and phone.startswith('8'):
        phone = '+7' + phone[1:]
    if len(phone) == 7:
        phone = '+7495' + phone
    return phone

def check_number(num, phone):
    return "YES" if num == phone else "NO"

print('----------------------------------------------------------------------\n Этот скрипт использует файл input.txt в кач-ве тел.книги\n Далее от вас потребуется ввести номер телефона, который вы хотите добавить в книгу\n Номер можете вводить используя скобки, дефисы, пробелы\n В случае ошибки, программа оповестит вас об этом')

def get_new_number():
    user_input = input('----------------------------------------------------------------------\nВведите новый номер телефона\n Или exit для того чтобы завершить работу программы\n')
    nuz = fix_phone(user_input)
    if user_input == 'exit':
        print('Программа завершается...')
        sys.exit()
    elif re.fullmatch(r'\+7\d{10}', nuz):
        print('Номер распознан')
    else:
        print('Команда или номер не распознаны, попробуйте еще раз')
        get_new_number()
    return nuz

while True:
    # Чтение входных данных из файла input.txt
    with open('input.txt', 'r') as file:
        phone_book = [line.strip() for line in file if line.strip()]

    # Нормализация телефонной книги
    for i in range(len(phone_book)):
        phone_book[i] = fix_phone(phone_book[i])

    # Ввод пользователя
    nuz = get_new_number()

    # Сравнение номеров
    if nuz in phone_book:
        print('Такой номер уже есть в тел.книге\nПопробуйте еще раз')
        continue
    else:
        print('Такого номера нет в тел.книге')

    # Запись нормализованной тел.книги + новый номер
    unique_phones = set(phone_book)
    unique_phones.add(nuz)
    with open('input.txt', 'w') as file:
        for phone in unique_phones:
            file.write(phone + '\n')
    print('Новый номер добавлен в телефонную книгу')
