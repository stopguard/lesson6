"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
    Известно, что при хранении данных используется принцип: одна строка — один пользователь.
    Разделитель между значениями — запятая.
    Написать код, загружающий данные из обоих файлов и сохраняет объединенные данные в новый файл.
    Хобби пишем через двоеточие и пробел после ФИО.
    Реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
"""
from os.path import exists
from sys import argv
from random import randint, sample

hobbies_f = 'hobbies.csv'
users_f = 'users.csv'
users_hobbies_f = 'users_hobby.txt'


def clear_file(path):
    """Чистит целевой файл от данных"""
    clear_f = open(path, 'w')
    clear_f.close()


def file_lines_score(path):
    """Считает строки в файле path"""
    score = 0
    with open(path, 'a+', encoding='utf-8') as f3:
        f3.seek(0)
        for _ in f3:
            score += 1
    return score


def gen_hobbies(path):
    """Генерирует файл с путём path.
    Содержит строки состоящие из случайного списка хобби длинной от 1 до 3 элементов"""
    num_of_users = file_lines_score(users_f)
    while True:
        num_of_strings = input(f'Сколько строк с хобби сформировать?\n(строк в файле users.csv - {num_of_users})\n>>> ')
        if num_of_strings.isdigit() and int(num_of_strings):
            num_of_strings = int(num_of_strings)
            break
    clear_file(path)
    with open('hobbies to generator.txt', encoding='utf-8') as f1:
        content = f1.read()
        hobbies_list = content.splitlines()[1:]
        content = ''
    with open(path, 'a', encoding='utf-8') as f2:
        for i in range(num_of_strings):
            line2 = str(sample(hobbies_list, k=(randint(1, 3)))) \
                .replace('[', '').replace(']', '').replace(', ', ',').replace("'", '')
            f2.write(line2 + '\n')
        hobbies_list = []
    print('Список хобби для пользователей сгенерирован')


def gen_users_hobbies(users_path, hobbies_path, sum_path):
    """Создаёт файл с пользователями и хобби из двух файлов"""
    users_list_length = file_lines_score(users_path)
    hobbies_list_length = file_lines_score(hobbies_path)
    clear_file(sum_path)
    user_gen = read_file(users_path)
    hobby_gen = read_file(hobbies_path)
    for i in range(max(hobbies_list_length, users_list_length)):
        user = next(user_gen)
        if i < hobbies_list_length:
            hobby = next(hobby_gen)
        else:
            hobby = None
        user_hobby = f'{user}: {hobby}\n'
        with open(sum_path, 'a', encoding='utf-8') as saved_file:
            saved_file.write(user_hobby)
            print(user_hobby)
    print('Файл со списком пользователей-хобби сгенерирован')


def read_file(path):
    """Построчное чтение файла генератором"""
    with open(path, encoding='utf-8') as file:
        for string in file:
            yield string.strip()


if len(argv) == 2:
    if argv[1] == 'gen':
        gen_hobbies(hobbies_f)
    else:
        print('gen - сгенерировать списки хобби в файл по умолчанию\n'
              'gen <имя файла> - сгенерировать списки хобби в указанный файл\n'
              'copy_users или cu <имя файла> скопировать дефолтный список пользователей в указанный файл\n'
              '<файл пользователей> <файл хобби> <итоговый файл> - собрать пользователей и хобби в один файл\n'
              'осторожно - если список хобби больше списка пользователей, всё сломается!')
elif len(argv) == 3:
    if argv[1] == 'gen':
        gen_hobbies(argv[2])
    elif argv[1] == 'copy_users' or argv[1] == 'cu':
        clear_file(argv[2])
        import_file = read_file(users_f)
        for line in import_file:
            with open(argv[2], 'a', encoding='utf-8') as copy_file:
                copy_file.write(line + '\n')
        print('Список пользователей скопирован')
    else:
        print('Указаны неверные аргументы')
elif len(argv) > 3:
    if exists(argv[1]) and exists(argv[2]):
        gen_users_hobbies(argv[1], argv[2], argv[3])
    else:
        print('Вы указали не существующий файл')
else:
    gen_hobbies(hobbies_f)
    gen_users_hobbies(users_f, hobbies_f, users_hobbies_f)
