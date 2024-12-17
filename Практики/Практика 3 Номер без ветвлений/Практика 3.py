import re
from functools import partial

def fix_phone(phone_book):
    def normalize(phone):
        phone = re.sub(r'[\(\)\-\s]', '', phone)
        if phone.startswith('8') and len(phone) == 11:
            phone = '+7' + phone[1:]
        elif len(phone) == 7:
            phone = '+7495' + phone
        return phone

    return list(map(normalize, phone_book))

def check_number(num, phone):
    return "YES" if num == phone else "NO"

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