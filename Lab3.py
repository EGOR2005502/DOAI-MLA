import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Путь к файлу базы данных SQLite
db_file = 'car_database.db'

# ****************************
# Создание базы данных и таблиц (если их нет)
def create_database():
    # Если файл БД уже существует, удалить его (для отладки)
    if os.path.isfile(db_file):
        os.remove(db_file)

    # Подключение к базе данных (или создание новой)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Создание таблицы "Car" (Машина)
    cursor.execute('''CREATE TABLE IF NOT EXISTS Car (
        CarID INTEGER PRIMARY KEY,
        StartYear INTEGER NOT NULL,
        Model TEXT NOT NULL,
        Category TEXT NOT NULL,
        BasePrice REAL NOT NULL
    )''')

    # Создание таблицы "CarInstance" (Экземпляр_Авто)
    cursor.execute('''CREATE TABLE IF NOT EXISTS CarInstance (
        InstanceID INTEGER PRIMARY KEY,
        CarFK INTEGER NOT NULL,
        ManufactureDate TEXT NOT NULL,
        SerialNumber TEXT NOT NULL UNIQUE,
        DriveType TEXT NOT NULL,
        TransmissionType TEXT NOT NULL,
        FOREIGN KEY (CarFK) REFERENCES Car(CarID)
    )''')

    # Создание таблицы "Engine" (Двигатель)
    cursor.execute('''CREATE TABLE IF NOT EXISTS Engine (
        EngineID INTEGER PRIMARY KEY,
        CarInstanceFK INTEGER NOT NULL,
        SerialNumber TEXT NOT NULL UNIQUE,
        Volume REAL NOT NULL,
        Type TEXT NOT NULL,
        ManufactureYear INTEGER NOT NULL,
        Power INTEGER NOT NULL,
        FOREIGN KEY (CarInstanceFK) REFERENCES CarInstance(InstanceID)
    )''')

    # Внесение данных в таблицу "Car" (Машина)
    cars_data = [
        (2018, 'Lada Travel', 'SUV', 1.2),
        (2020, 'Lada Vesta', 'Sedan', 1.5),
        (2021, 'Lada Granta', 'Hatchback', 0.95),
        (2022, 'Lada Granta', 'SUV', 1.8),
        (2025, 'Lada Vesta', 'Sport', 2.2)
    ]
    cursor.executemany("INSERT INTO Car (StartYear, Model, Category, BasePrice) VALUES (?, ?, ?, ?)", cars_data)

    # Внесение данных в таблицу "CarInstance" (Экземпляр_Авто)
    car_instances_data = [
        (1, '2020-01-15', 'SN12345', 'AWD', 'Automatic'),
        (1, '2020-06-20', 'SN12346', 'AWD', 'Manual'),
        (2, '2021-03-10', 'SN22345', 'FWD', 'Automatic'),
        (3, '2021-07-22', 'SN32345', 'RWD', 'Automatic'),
        (4, '2025-01-10', 'SN34345', 'RWD', 'Automatic')
    ]
    cursor.executemany("INSERT INTO CarInstance (CarFK, ManufactureDate, SerialNumber, DriveType, TransmissionType) VALUES (?, ?, ?, ?, ?)", car_instances_data)

    # Внесение данных в таблицу "Engine" (Двигатель)
    engines_data = [
        (1, 'NG12345', 2.0, 'Gasoline', 2020, 150),
        (2, 'ENG22345', 3.0, 'Electric', 2021, 200),
        (3, 'ENG32345', 1.8, 'Hybrid', 2021, 140),
        (4, 'ENG12346', 2.5, 'Diesel', 2020, 180),
        (5, 'ENG35345', 2.5, 'Hybrid', 2024, 220)
    ]
    cursor.executemany("INSERT INTO Engine (CarInstanceFK, SerialNumber, Volume, Type, ManufactureYear, Power) VALUES (?, ?, ?, ?, ?, ?)", engines_data)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

# ****************************
# Функция для отображения таблицы Car
def show_car_table():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для таблицы Car
    car_window = tk.Toplevel()
    car_window.title("Таблица Car")
    car_window.geometry("600x400")

    # Функция для возврата в главное меню
    def back_to_main():
        car_window.destroy()  # Закрытие текущего окна
        root.deiconify()  # Показ главного окна

    # Создание Treeview для отображения таблицы Car
    columns = ("CarID", "StartYear", "Model", "Category", "BasePrice")
    tree = ttk.Treeview(car_window, columns=columns, show="headings")

    # Настройка заголовков столбцов
    tree.heading("CarID", text="ID")
    tree.heading("StartYear", text="Год выпуска")
    tree.heading("Model", text="Модель")
    tree.heading("Category", text="Категория")
    tree.heading("BasePrice", text="Базовая цена")

    # Настройка ширины столбцов
    tree.column("CarID", width=50, anchor="center")
    tree.column("StartYear", width=100, anchor="center")
    tree.column("Model", width=150, anchor="center")
    tree.column("Category", width=150, anchor="center")
    tree.column("BasePrice", width=100, anchor="center")

    # Размещение Treeview в окне
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Подключение к базе данных и заполнение Treeview
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Car")
    results = cursor.fetchall()
    for result in results:
        tree.insert("", "end", values=result)
    conn.close()

    # Кнопка "Назад"
    back_button = tk.Button(car_window, text="Назад", command=back_to_main)
    back_button.pack(pady=10)

# ****************************
# Функция для отображения таблицы CarInstance (Задание 1)
def show_car_instance_table():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для таблицы CarInstance
    car_instance_window = tk.Toplevel()
    car_instance_window.title("Таблица CarInstance")
    car_instance_window.geometry("800x400")

    # Функция для возврата в главное меню
    def back_to_main():
        car_instance_window.destroy()  # Закрытие текущего окна
        root.deiconify()  # Показ главного окна

    # Создание Treeview для отображения таблицы CarInstance
    columns = ("InstanceID", "CarFK", "ManufactureDate", "SerialNumber", "DriveType", "TransmissionType")
    tree = ttk.Treeview(car_instance_window, columns=columns, show="headings")

    # Настройка заголовков столбцов
    tree.heading("InstanceID", text="ID экземпляра")
    tree.heading("CarFK", text="ID машины")
    tree.heading("ManufactureDate", text="Дата производства")
    tree.heading("SerialNumber", text="Серийный номер")
    tree.heading("DriveType", text="Тип привода")
    tree.heading("TransmissionType", text="Тип трансмиссии")

    # Настройка ширины столбцов
    tree.column("InstanceID", width=100, anchor="center")
    tree.column("CarFK", width=100, anchor="center")
    tree.column("ManufactureDate", width=150, anchor="center")
    tree.column("SerialNumber", width=150, anchor="center")
    tree.column("DriveType", width=100, anchor="center")
    tree.column("TransmissionType", width=150, anchor="center")

    # Размещение Treeview в окне
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Подключение к базе данных и заполнение Treeview
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CarInstance")
    results = cursor.fetchall()
    for result in results:
        tree.insert("", "end", values=result)
    conn.close()

    # Кнопка "Назад"
    back_button = tk.Button(car_instance_window, text="Назад", command=back_to_main)
    back_button.pack(pady=10)

# ****************************
# Функция для отображения таблицы Engine (Задание 2)
def show_engine_table():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для таблицы Engine
    engine_window = tk.Toplevel()
    engine_window.title("Таблица Engine")
    engine_window.geometry("900x400")

    # Функция для возврата в главное меню
    def back_to_main():
        engine_window.destroy()  # Закрытие текущего окна
        root.deiconify()  # Показ главного окна

    # Создание Treeview для отображения таблицы Engine
    columns = ("EngineID", "CarInstanceFK", "SerialNumber", "Volume", "Type", "ManufactureYear", "Power")
    tree = ttk.Treeview(engine_window, columns=columns, show="headings")

    # Настройка заголовков столбцов
    tree.heading("EngineID", text="ID двигателя")
    tree.heading("CarInstanceFK", text="ID экземпляра")
    tree.heading("SerialNumber", text="Серийный номер")
    tree.heading("Volume", text="Объем")
    tree.heading("Type", text="Тип")
    tree.heading("ManufactureYear", text="Год выпуска")
    tree.heading("Power", text="Мощность")

    # Настройка ширины столбцов
    tree.column("EngineID", width=100, anchor="center")
    tree.column("CarInstanceFK", width=100, anchor="center")
    tree.column("SerialNumber", width=150, anchor="center")
    tree.column("Volume", width=100, anchor="center")
    tree.column("Type", width=100, anchor="center")
    tree.column("ManufactureYear", width=100, anchor="center")
    tree.column("Power", width=100, anchor="center")

    # Размещение Treeview в окне
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Подключение к базе данных и заполнение Treeview
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Engine")
    results = cursor.fetchall()
    for result in results:
        tree.insert("", "end", values=result)
    conn.close()

    # Кнопка "Назад"
    back_button = tk.Button(engine_window, text="Назад", command=back_to_main)
    back_button.pack(pady=10)

# ****************************
# Функция для выбора столбцов и отображения таблицы CarInstance (Задание 3)
def show_car_instance_selected_columns():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для выбора столбцов
    select_columns_window = tk.Toplevel()
    select_columns_window.title("Выбор столбцов CarInstance")
    select_columns_window.geometry("300x200")

    # Переменные для хранения состояния чекбоксов
    columns_to_show = {
        "InstanceID": tk.BooleanVar(),
        "CarFK": tk.BooleanVar(),
        "ManufactureDate": tk.BooleanVar(),
        "SerialNumber": tk.BooleanVar(),
        "DriveType": tk.BooleanVar(),
        "TransmissionType": tk.BooleanVar()
    }

    # Создание чекбоксов для выбора столбцов
    for column, var in columns_to_show.items():
        cb = tk.Checkbutton(select_columns_window, text=column, variable=var)
        cb.pack(anchor="w")

    # Функция для отображения выбранных столбцов
    def show_selected_columns():
        # Получение выбранных столбцов
        selected_columns = [column for column, var in columns_to_show.items() if var.get()]
        if not selected_columns:
            messagebox.showwarning("Ошибка", "Выберите хотя бы один столбец!")
            return

        # Закрытие окна выбора столбцов
        select_columns_window.destroy()

        # Создание нового окна для отображения выбранных столбцов
        car_instance_selected_window = tk.Toplevel()
        car_instance_selected_window.title("Задание 3: Выбранные столбцы CarInstance")
        car_instance_selected_window.geometry("800x400")

        # Функция для возврата в главное меню
        def back_to_main():
            car_instance_selected_window.destroy()  # Закрытие текущего окна
            root.deiconify()  # Показ главного окна

        # Создание Treeview для отображения выбранных столбцов
        tree = ttk.Treeview(car_instance_selected_window, columns=selected_columns, show="headings")

        # Настройка заголовков столбцов
        for column in selected_columns:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        # Размещение Treeview в окне
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Подключение к базе данных и заполнение Treeview
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT {', '.join(selected_columns)} FROM CarInstance")
        results = cursor.fetchall()
        for result in results:
            tree.insert("", "end", values=result)
        conn.close()

        # Кнопка "Назад"
        back_button = tk.Button(car_instance_selected_window, text="Назад", command=back_to_main)
        back_button.pack(pady=10)

    # Кнопка "Показать выбранные столбцы"
    show_button = tk.Button(select_columns_window, text="Показать выбранные столбцы", command=show_selected_columns)
    show_button.pack(pady=10)

    # Кнопка "Назад"
    back_button = tk.Button(select_columns_window, text="Назад", command=lambda: [select_columns_window.destroy(), root.deiconify()])
    back_button.pack(pady=10)

# ****************************
# Функция для выбора столбцов и отображения таблицы Engine (Задание 4)
def show_engine_selected_columns():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для выбора столбцов
    select_columns_window = tk.Toplevel()
    select_columns_window.title("Выбор столбцов Engine")
    select_columns_window.geometry("300x300")

    # Переменные для хранения состояния чекбоксов
    columns_to_show = {
        "EngineID": tk.BooleanVar(),
        "CarInstanceFK": tk.BooleanVar(),
        "SerialNumber": tk.BooleanVar(),
        "Volume": tk.BooleanVar(),
        "Type": tk.BooleanVar(),
        "ManufactureYear": tk.BooleanVar(),
        "Power": tk.BooleanVar()
    }

    # Создание чекбоксов для выбора столбцов
    for column, var in columns_to_show.items():
        cb = tk.Checkbutton(select_columns_window, text=column, variable=var)
        cb.pack(anchor="w")

    # Функция для отображения выбранных столбцов
    def show_selected_columns():
        # Получение выбранных столбцов
        selected_columns = [column for column, var in columns_to_show.items() if var.get()]
        if not selected_columns:
            messagebox.showwarning("Ошибка", "Выберите хотя бы один столбец!")
            return

        # Закрытие окна выбора столбцов
        select_columns_window.destroy()

        # Создание нового окна для отображения выбранных столбцов
        engine_selected_window = tk.Toplevel()
        engine_selected_window.title("Задание 4: Выбранные столбцы Engine")
        engine_selected_window.geometry("900x400")

        # Функция для возврата в главное меню
        def back_to_main():
            engine_selected_window.destroy()  # Закрытие текущего окна
            root.deiconify()  # Показ главного окна

        # Создание Treeview для отображения выбранных столбцов
        tree = ttk.Treeview(engine_selected_window, columns=selected_columns, show="headings")

        # Настройка заголовков столбцов
        for column in selected_columns:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        # Размещение Treeview в окне
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Подключение к базе данных и заполнение Treeview
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT {', '.join(selected_columns)} FROM Engine")
        results = cursor.fetchall()
        for result in results:
            tree.insert("", "end", values=result)
        conn.close()

        # Кнопка "Назад"
        back_button = tk.Button(engine_selected_window, text="Назад", command=back_to_main)
        back_button.pack(pady=10)

    # Кнопка "Показать выбранные столбцы"
    show_button = tk.Button(select_columns_window, text="Показать выбранные столбцы", command=show_selected_columns)
    show_button.pack(pady=10)

    # Кнопка "Назад"
    back_button = tk.Button(select_columns_window, text="Назад", command=lambda: [select_columns_window.destroy(), root.deiconify()])
    back_button.pack(pady=10)

# ****************************
# Функция для поиска по таблице CarInstance
def search_car_instance():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для поиска
    search_window = tk.Toplevel()
    search_window.title("Поиск по экземплярам авто")
    search_window.geometry("400x200")

    # Функция для возврата в главное меню
    def back_to_main():
        search_window.destroy()  # Закрытие текущего окна
        root.deiconify()  # Показ главного окна

    # Поле для ввода значения поиска
    search_label = tk.Label(search_window, text="Введите значение для поиска:")
    search_label.pack(pady=10)

    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=10)

    # Функция для выполнения поиска
    def perform_search():
        search_value = search_entry.get().strip()
        if not search_value:
            messagebox.showwarning("Ошибка", "Введите значение для поиска!")
            return

        # Подключение к базе данных
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Поиск по всем столбцам таблицы CarInstance
        cursor.execute(f"""
            SELECT * FROM CarInstance
            WHERE InstanceID LIKE ? OR
                  CarFK LIKE ? OR
                  ManufactureDate LIKE ? OR
                  SerialNumber LIKE ? OR
                  DriveType LIKE ? OR
                  TransmissionType LIKE ?
        """, (f"%{search_value}%",) * 6)

        results = cursor.fetchall()
        conn.close()

        if not results:
            messagebox.showinfo("Результат", "Ничего не найдено.")
            return

        # Создание нового окна для отображения результатов
        result_window = tk.Toplevel()
        result_window.title("Результаты поиска")
        result_window.geometry("1000x400")

        # Создание Treeview для отображения результатов
        columns = ("InstanceID", "CarFK", "ManufactureDate", "SerialNumber", "DriveType", "TransmissionType")
        tree = ttk.Treeview(result_window, columns=columns, show="headings")

        # Настройка заголовков столбцов
        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        # Размещение Treeview в окне
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Заполнение Treeview результатами
        for result in results:
            tree.insert("", "end", values=result)

        # Кнопка "Назад"
        back_button = tk.Button(result_window, text="Назад", command=result_window.destroy)
        back_button.pack(pady=10)

    # Кнопка "Поиск"
    search_button = tk.Button(search_window, text="Поиск", command=perform_search)
    search_button.pack(pady=10)

    # Кнопка "Назад"
    back_button = tk.Button(search_window, text="Назад", command=back_to_main)
    back_button.pack(pady=10)

# ****************************
# Функция для поиска по таблице Engine
def search_engine():
    # Закрытие главного окна
    root.withdraw()

    # Создание нового окна для поиска
    search_window = tk.Toplevel()
    search_window.title("Поиск по двигателям")
    search_window.geometry("400x200")

    # Функция для возврата в главное меню
    def back_to_main():
        search_window.destroy()  # Закрытие текущего окна
        root.deiconify()  # Показ главного окна

    # Поле для ввода значения поиска
    search_label = tk.Label(search_window, text="Введите значение для поиска:")
    search_label.pack(pady=10)

    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=10)

    # Функция для выполнения поиска
    def perform_search():
        search_value = search_entry.get().strip()
        if not search_value:
            messagebox.showwarning("Ошибка", "Введите значение для поиска!")
            return

        # Подключение к базе данных
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Поиск по всем столбцам таблицы Engine
        cursor.execute(f"""
            SELECT * FROM Engine
            WHERE EngineID LIKE ? OR
                  CarInstanceFK LIKE ? OR
                  SerialNumber LIKE ? OR
                  Volume LIKE ? OR
                  Type LIKE ? OR
                  ManufactureYear LIKE ? OR
                  Power LIKE ?
        """, (f"%{search_value}%",) * 7)

        results = cursor.fetchall()
        conn.close()

        if not results:
            messagebox.showinfo("Результат", "Ничего не найдено.")
            return

        # Создание нового окна для отображения результатов
        result_window = tk.Toplevel()
        result_window.title("Результаты поиска")
        result_window.geometry("1200x400")

        # Создание Treeview для отображения результатов
        columns = ("EngineID", "CarInstanceFK", "SerialNumber", "Volume", "Type", "ManufactureYear", "Power")
        tree = ttk.Treeview(result_window, columns=columns, show="headings")

        # Настройка заголовков столбцов
        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, width=150, anchor="center")

        # Размещение Treeview в окне
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Заполнение Treeview результатами
        for result in results:
            tree.insert("", "end", values=result)

        # Кнопка "Назад"
        back_button = tk.Button(result_window, text="Назад", command=result_window.destroy)
        back_button.pack(pady=10)

    # Кнопка "Поиск"
    search_button = tk.Button(search_window, text="Поиск", command=perform_search)
    search_button.pack(pady=10)

    # Кнопка "Назад"
    back_button = tk.Button(search_window, text="Назад", command=back_to_main)
    back_button.pack(pady=10)

# ****************************
# Главное окно
root = tk.Tk()
root.title("Главное меню")
root.geometry("300x400")

# Создание базы данных (если её нет)
create_database()

# Кнопка "Показать пример" (для таблицы Car)
show_car_button = tk.Button(root, text="Показать пример", command=show_car_table)
show_car_button.pack(pady=10)

# Кнопка "Задание 1" (для таблицы CarInstance)
task1_button = tk.Button(root, text="Задание 1", command=show_car_instance_table)
task1_button.pack(pady=10)

# Кнопка "Задание 2" (для таблицы Engine)
task2_button = tk.Button(root, text="Задание 2", command=show_engine_table)
task2_button.pack(pady=10)

# Кнопка "Задание 3" (для выбора столбцов CarInstance)
task3_button = tk.Button(root, text="Задание 3", command=show_car_instance_selected_columns)
task3_button.pack(pady=10)

# Кнопка "Задание 4" (для выбора столбцов Engine)
task4_button = tk.Button(root, text="Задание 4", command=show_engine_selected_columns)
task4_button.pack(pady=10)

# Кнопка "Поиск по экземплярам авто"
search_car_instance_button = tk.Button(root, text="Поиск по экземплярам авто", command=search_car_instance)
search_car_instance_button.pack(pady=10)

# Кнопка "Поиск по двигателям"
search_engine_button = tk.Button(root, text="Поиск по двигателям", command=search_engine)
search_engine_button.pack(pady=10)

# Запуск главного цикла обработки событий
root.mainloop()