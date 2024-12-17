def fix_phone(phone_book):
    for i in range(len(phone_book)):
        phone_book[i] = phone_book[i].replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if len(phone_book[i]) == 11 and phone_book[i].startswith('8'):
            phone_book[i] = '+7' + phone_book[i][1:]
        if len(phone_book[i]) == 7:
            phone_book[i] = '+7495' + phone_book[i]
    return phone_book

def check_number(num, phone):
    return "YES" if num == phone else "NO"

# Чтение входных данных из файла input.txt
with open('input.txt', 'r') as file:
    new_phone = file.readline().strip()
    phone_book = [line.strip() for line in file if line.strip()]

# Нормализация номеров
phone_book = fix_phone(phone_book)
new_phone = fix_phone([new_phone])[0]

# Сравнение номеров и запись результата в файл output.txt
with open('output.txt', 'w') as file:
    for phone in phone_book:
        file.write(check_number(new_phone, phone) + '\n')

# Запись уникальных нормализованных номеров в файл filtered.txt
unique_phones = set(phone_book)
unique_phones.add(new_phone)
with open('filtered.txt', 'w') as file:
    for phone in unique_phones:
        file.write(phone + '\n')