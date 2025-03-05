import re
from functools import partial

def fix_phone(phone_book):
    def normalize(phone):
        phone = re.sub(r'[\(\)\-\s]', '', phone)
        return {
            11: lambda: '+7' + phone[1:],
            7: lambda: '+7495' + phone
        }.get(len(phone), lambda: phone)()

    return list(map(normalize, phone_book))

def check_number(num, phone):
    return {
        True: "YES",
        False: "NO"
    }[num == phone]

# Чтение входных данных из файла input.txt
with open('input.txt', 'r') as file:
    new_phone = file.readline().strip()
    phone_book = list(map(str.strip, file.readlines()))

# Нормализация номеров
phone_book = fix_phone(phone_book)
new_phone = fix_phone([new_phone])[0]

# Сравнение номеров и запись результата в файл output.txt
check_number_partial = partial(check_number, new_phone)
results = list(map(check_number_partial, phone_book))
with open('output.txt', 'w') as file:
    file.write('\n'.join(results) + '\n')

# Запись уникальных нормализованных номеров в файл filtered.txt
unique_phones = set(phone_book)
unique_phones.add(new_phone)
with open('filtered.txt', 'w') as file:
    file.write('\n'.join(unique_phones) + '\n')