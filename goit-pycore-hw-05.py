'''
Завдання 1

Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду. Тобто, 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, і так далі.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.

Вимоги до завдання:

Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
Використання рекурсії для обчислення чисел Фібоначчі.

Рекомендації для виконання:

Ось псевдокод для функції caching_fibonacci, яка обчислює числа Фібоначчі з використанням кешування:

ФУНКЦІЯ caching_fibonacci
    Створити порожній словник cache

    ФУНКЦІЯ fibonacci(n)
        Якщо n <= 0, повернути 0
        Якщо n == 1, повернути 1
        Якщо n у cache, повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Повернути cache[n]

    Повернути функцію fibonacci
КІНЕЦЬ ФУНКЦІЇ caching_fibonacci

Функція caching_fibonacci створює внутрішню функцію fibonacci і словник cache для зберігання результатів обчислення чисел Фібоначчі. Кожен раз, коли викликається fibonacci(n), спочатку перевіряється, чи вже збережено значення для n у cache. Якщо значення є у кеші, воно повертається негайно, що значно зменшує кількість рекурсивних викликів. Якщо значення відсутнє у кеші, воно обчислюється рекурсивно і зберігається у cache. Функція caching_fibonacci повертає внутрішню функцію fibonacci, яка тепер може бути використана для обчислення чисел Фібоначчі з використанням кешування.

Критерії оцінювання:
Коректність реалізації функції fibonacci(n) з урахуванням використання кешу.
Ефективне використання рекурсії та кешування для оптимізації обчислень.
Чистота коду, включаючи читабельність та наявність коментарів.

Приклад використання:
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

У цьому прикладі, коли ви викликаєте fib(10) або fib(15), функція fibonacci всередині caching_fibonacci обчислює відповідні числа Фібоначчі, зберігаючи попередні результати у кеші. Це робить повторні виклики для тих самих значень n значно швидшими, оскільки вони просто повертають значення з кешу. Замикання дозволяє fibonacci(n) "пам'ятати" стан cache між різними викликами, що є ключовим для кешування результатів обчислень

'''
from typing import Callable
def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n, * arg) -> int|None:
        try:
            n = int(n)
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        except ValueError:
            print('Please enter a number')
            return None
        except TypeError:
            print('Please enter a number')
            return None

    return fibonacci

fib = caching_fibonacci()

assert fib(10) == 55
assert fib(15) == 610
assert fib(10,45) == 55
assert fib('15') == 610
assert fib(0) == 0
assert fib(-15) == 0
assert fib(15.5445) == 610
assert fib([23,23,23]) == None
assert fib({"n":10}) == None

'''
Завдання 2

Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

Вимоги до завдання:
Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.


Рекомендації для виконання:
Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, що числа чітко відокремлені пробілами.
Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.


Критерії оцінювання:
Правильність визначення та повернення дійсних чисел функцією generator_numbers.
Коректність обчислення загальної суми в sum_profit.
Чистота коду, наявність коментарів та відповідність стилю кодування PEP8.

Приклад використання:

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

Очікуване виведення:
Загальний дохід: 1351.46
'''
from typing import Generator
from typing import Callable
from termcolor import colored

# Generator визначає функцію-генератор, яка повертає об'єкт типу Generator.
# Видає значення типу float (це перший параметр).
# Не приймає значень у send() (другий параметр, тут None).
# Не повертає значення в return (третій параметр, теж None).

def generator_numbers(text: str) -> Generator[float, None, None]:
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            continue  

def sum_profit(text: str, parser: Callable[[str], Generator[float, None, None]]) -> float:
    return round(sum(parser(text)),2)


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. 453 435354"
total_income = sum_profit(text, generator_numbers)
print(colored(f"Загальний дохід: {total_income}",'green'))
text2 = "Загальний дохід працівника складається з декількох частин: 1000.0145 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.0045 доларів. 453 435354"
total_income2 = sum_profit(text2, generator_numbers)
print(colored(f"Загальний дохід: {total_income2}",'green'))

'''
Завдання 3 (не обов'язкове)

Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.

Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

Для виконання завдання візьміть наступний приклад лог-файлу:

2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.

Вимоги до завдання:

Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записів певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.

Рекомендації для виконання:
Перш ніж почати, ознайомтеся зі структурою вашого лог-файлу. Зверніть увагу на формат дати та часу, рівні логування INFO, ERROR, DEBUG, WARNING і структуру повідомлень.
Зрозумійте, як розділені різні компоненти логу, це зазвичай пробіли або спеціальні символи.
Розділіть ваше завдання на логічні блоки і функції для кращої читабельності і подальшого розширення.
Парсинг рядка логу виконує ****функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список.
Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. Вона дозволить вам отримати всі записи логу для певного рівня логування.
Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, яка проходить по всім записам і підраховує кількість записів для кожного рівня логування.
Вивід результатів виконайте за допомоги функції display_log_counts(counts: dict), яка форматує та виводить результати підрахунку в читабельній формі.
Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.

Критерії оцінювання:
Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
Скрипт коректно обробляє помилки, такі як неправильний формат лог-файлу або відсутність файлу.
При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функція, списковий вираз, функція filter, тощо.
Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.

Приклад використання:

При запуску скрипту
python [main.py](<http://main.py/>) /path/to/logfile.log
Ми повинні очікувати наступне виведення

Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Якщо користувач хоче переглянути всі записи певного рівня логування, він може запустити скрипт з додатковим аргументом, наприклад:

python main.py path/to/logfile.log error

Це виведе загальну статистику за рівнями, а також детальну інформацію для всіх записів з рівнем ERROR.

Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
'''

# Case 1 - can't create with generators
# Case 2 - create with generators

# CASE 1
import argparse
from termcolor import colored

# count logs by level
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

# display log counts
def display_log_counts(counts: dict, log_type: str = None):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        if log_type and level.lower() == log_type.lower():  
            print(colored(f"{level:<16} | {count}", 'light_magenta'))  
        else:
            print(f'{level:<16} | {count}')

# parser for line in logfile
def parse_log_line(line: str) -> dict:
    try:
        date, time, level, message = line.split(' ', maxsplit=3)
        return {        
            'date': date,
            'time': time,
            'level': level,
            'message': message
        }
    except ValueError:
        return None 

# read file with logs
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line: 
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"{colored('File not found:', 'red')} {colored(file_path, 'red')}")
    return logs


# filtering by logging level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def main():
    parser = argparse.ArgumentParser(description="Process a log file for a specific log type.")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("log", nargs="?", help="Type of log for filter", default=None)
    try: 
        args = parser.parse_args()
        print(f"{colored('Log file path:', 'light_blue')} {colored(args.logfile, 'green')}")
        print(f"{colored('Log type:', 'light_blue')} {colored(args.log, 'green') if args.log else 'None'}")
    except SystemExit:
        print(f"{colored('Invalid arguments.', 'red')}")
        return

    logs = load_logs(args.logfile)

    if logs:
        counts = count_logs_by_level(logs)
        display_log_counts(counts, args.log)
        if args.log:
            logs = filter_logs_by_level(logs, args.log)
            print(f"{colored('Деталі логів для рівня:{args.log}', 'light_blue')}")
            if len(logs) == 0:
                print(f"{colored('No logs found for this level.', 'red')}")
            for log in logs:
                print(f"{log['date']} {log['time']} - {log['message']}", end="")


if __name__ == "__main__":
    main()

# CASE 2
import argparse
from termcolor import colored

# count logs by level
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

# display log counts
def display_log_counts(counts: dict, log_type: str = None):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        if log_type and level.lower() == log_type.lower():  
            print(colored(f"{level:<16} | {count}", 'light_magenta'))  
        else:
            print(f'{level:<16} | {count}')

# parser for line in logfile
def parse_log_line(line: str) -> dict:
    try:
        date, time, level, message = line.split(' ', maxsplit=3)
        return {        
            'date': date,
            'time': time,
            'level': level,
            'message': message
        }
    except ValueError:
        return None


# read file with logs (generator)
def load_logs(file_path: str):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    yield parsed_line
    except FileNotFoundError:
        print(f"{colored('File not found:', 'red')} {colored(file_path, 'red')}")


# filtering by logging level (generator)
def filter_logs_by_level(logs, level: str):
    for log in logs:
        if log['level'].lower() == level.lower():
            yield log  


def main():
    parser = argparse.ArgumentParser(description="Process a log file for a specific log type.")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("log", nargs="?", help="Type of log for filter", default=None)
    try: 
        args = parser.parse_args()
        print(f"{colored('Log file path:', 'light_blue')} {colored(args.logfile, 'green')}")
        print(f"{colored('Log type:', 'light_blue')} {colored(args.log, 'green') if args.log else 'None'}")
    except SystemExit:
        print(f"{colored('Invalid arguments.', 'red')}")
        return
    logs = list(load_logs(args.logfile))

    if logs:
        counts = count_logs_by_level(logs)
        display_log_counts(counts, args.log)
        if args.log:
            logs = list(filter_logs_by_level(logs, args.log))              
            print(colored(f'Деталі логів для рівня: {args.log}', 'light_blue'))
            if len(logs) == 0:
                print(f"{colored('No logs found for this level.', 'red')}")
            for log in logs:
                print(f"{log['date']} {log['time']} - {log['message']}", end="")

if __name__ == "__main__":
    main()

'''
Завдання 4

Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

Вимоги до завдання:

Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.

Рекомендації для виконання:

В якості прикладу додамо декоратор input_error для обробки помилки ValueError
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.

Критерії оцінювання:
Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.

Приклад використання:
При запуску скрипту діалог з ботом повинен бути схожим на цей.

Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356 
Enter a command:
'''

from termcolor import colored
from typing import Callable, Any
import os
from functools import wraps

path = "./contacts.txt"

# add error decorator
def input_error(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return colored("Give me name and phone please.", 'red')
        except KeyError:
            return colored("Enter user name.", 'red')
        except IndexError:
            return colored("Give me name and phone please.", 'red')
        except Exception as e:
            return colored(f"An error occurred: {e}", 'red')
        
    return inner

# for comands - delete spaces and convert to lower case
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# read contacts from file
def file_read():
    contacts = {}
    if not os.path.exists(path):
        print(f"{colored('File not found', 'red')}")
        return contacts
    try:
        with open(path, 'r', encoding="utf-8") as f:
            unsorted_contacts = {}
            for line in f:
                if not line.strip():
                    print(f"{colored('List has an empty line', 'red')}")
                    continue
                try:
                    parts = line.strip().split(',')
                    if len(parts) != 2:  
                        print(f"{colored('Invalid line format:', 'yellow')} {colored(line.strip(), 'red')}")
                        continue
                    name, phone = parts
                    try:
                        phone = int(phone)
                        if phone:
                            unsorted_contacts[name] = phone
                        else:
                            print(f"{colored('Check data for name:', 'yellow')}{colored(name, 'red')}{colored(', phone:', 'yellow')}{colored(phone, 'red')}")
                    except ValueError:
                        print(f"{colored('Invalid phone value:', 'yellow')} {colored(phone, 'red')}")
                        continue
                except ValueError:
                    print(f"{colored('Check data for', 'yellow')} {colored(line.strip(), 'red')}")
                    continue
            contacts = dict(sorted(unsorted_contacts.items()))
            return contacts
    except FileNotFoundError:
        print(f"{colored('File not found', 'red')}")

# write contacts to file
@input_error
def file_write(contacts):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            for name, phone in contacts.items():
                f.write(f"{name},{phone}\n")
    except Exception as e:
        print(f"{colored("An error occurred while saving contacts:", 'yellow')} {colored(e, 'red')}")
        

# add contact to the contacts (file)
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return colored("Invalid name or phone for add.", 'red')
    name, phone = args
    for key in contacts:
        if key == name:
            return f"{colored('Contact already exists:', 'yellow')} {colored(name, 'red')}"
    try:
        phone = int(phone)
        contacts[name] = phone
        file_write(contacts)
        print(colored(f"Contact added successfully.", 'green'))
        return contacts
    except ValueError:
        return f"{colored('Invalid phone value:', 'yellow')} {colored(phone, 'red')}"


#change contact phone
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return f"{colored('Invalid name or phone:', 'yellow')} {colored(args, 'red')}"
    name, new_phone = args
    if name not in contacts:
        return(f"{colored("The name", 'yellow')} {colored("'",'red')}{colored(name, 'red')}{colored("'",'red')} {colored("does not exist in the contacts.", 'yellow')}")
    try:
        new_phone = int(new_phone)
        if new_phone is None:
            return f"{colored('Check data for name:', 'yellow')}{colored(name, 'red')}{colored(', phone:', 'yellow')}{colored(new_phone, 'red')}"
        else:
            contacts[name] = new_phone
            file_write(contacts)
            print(colored(f"Contact '{name}' updated successfully.", 'green'))
            return contacts
    except ValueError:
        return f"{colored('Invalid phone value:', 'yellow')} {colored(new_phone, 'red')}"
    
#rename contact phone
@input_error
def rename_contact(args, contacts):
    if len(args) != 2:
        return f"{colored('Invalid names:', 'yellow')} {colored(args, 'red')}"
    old_name, new_name = args
    if old_name not in contacts:
        return(f"{colored("The name", 'yellow')} {colored("'",'red')}{colored(old_name, 'red')}{colored("'",'red')} {colored("does not exist in the contacts.", 'yellow')}")

    contacts[new_name] = contacts.pop(old_name)
    file_write(contacts)
    print(colored(f"Contact '{old_name}' renamed to '{new_name}' successfully.", 'green'))
    return contacts

#delete contact phone
@input_error
def delete_contact(args, contacts):
    if len(args) != 1:
        return f"{colored('Invalid name:', 'yellow')} {colored(args, 'red')}"
    contact_name = args[0]
    if contact_name not in contacts:
        return(f"{colored("The name", 'yellow')} {colored("'",'red')}{colored(contact_name, 'red')}{colored("'",'red')} {colored("does not exist in the contacts.", 'yellow')}")

    del contacts[contact_name]
    file_write(contacts)
    print(colored(f"Contact '{contact_name}' deleted successfully.", 'green'))
    return contacts

#show phone by name
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return f"{colored('Invalid arguments:', 'yellow')} {colored(args, 'red')}"
    name = args[0]
    if name in contacts:
        return colored(f"phone {name}: {contacts[name]}", 'light_green')
    else:
        return f"{colored('Name not found:', 'yellow')} {colored(name, 'red')}"

#show all contacts
@input_error
def show_all(contacts):
    if not contacts:
        return f"{colored('No contacts found', 'yellow')}"
    else:
        for name, phone in contacts.items():
            print(f"{colored(name, 'light_green')}: {colored(phone, 'light_green')}")
        return f"{colored("All contacts:", "green")}{contacts}"

def main():
    contacts = file_read()
    print(colored("Welcome to the assistant bot!", 'green'))
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(colored("Good bye!", 'green'))
            break
        elif command == "hello": # say hello
            print("How can I help you?")
        elif command == "add": # add contact (name, phone)
            print(add_contact(args, contacts))
        elif command == "phone": # show phone by name (name)
            print(show_phone(args, contacts))
        elif command == "change": # change phone by name (name, new phone)
            print(change_contact(args, contacts))
        elif command == "rename": # rename contact (old name, new name)
            print(rename_contact(args, contacts))
        elif command == "delete": # delete contact (name)
            print(delete_contact(args, contacts))
        elif command == "all": # show all contacts
            print(show_all(contacts))
        else:
            print(colored("Invalid command. Please try again.", "red"))

if __name__ == "__main__":
    main()