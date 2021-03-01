"""
Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение.
    Данные хранить в файле bakery.csv в кодировке utf-8.
    Нумерация записей начинается с 1.
    Файл не должен читаться целиком.
    Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
from sys import argv        # импортируем список аргументов


def reset_file(path):
    """Очищает содержимое файла"""
    clear = open(path, 'w')
    clear.close()


def edit(num_of_string, new_value):
    """Заменяет данные в строке num_of_string на new_value"""
    reset_file('buffer.dat')                            # чистим буферный файл
    found_line = False                                  # информация о том найдена ли строка
    output = 'Неизвестная ошибка.'                      # Выходные данные на данный момент
    with open('bakery.csv', encoding='utf-8') as f:     # открываем файл
        line = f.readline()                                 # читаем первую строку
        i = 1                                               # ее номер
        while line:                                         # пока линия не пуста
            if i != num_of_string:                              # и строка не равна искомой
                with open('buffer.dat', 'a', encoding='utf-8') as buffer:   # пишем ее в буферный файл
                    buffer.write(line)
            else:                                               # если равна искомой
                with open('buffer.dat', 'a', encoding='utf-8') as buffer:   # записываем в буфер new_value
                    buffer.write(new_value + '\n')
                found_line = True                                           # и указываем что строка найдена
            line = f.readline()                                         # читаем следующую строку
            i += 1                                                      # переключаем ее номер
    if found_line:                                              # если строка найдена
        reset_file('bakery.csv')                                    # чистим файл
        with open('buffer.dat', encoding='utf-8') as return_data:   # переливаем в него данные из буфера
            for data in return_data:
                with open('bakery.csv', 'a', encoding='utf-8') as save_data:
                    save_data.write(data)
        output = 'Данные успешно записаны в указанную строку.'      # меняем результат работы функции
    else:                                                       # если строка не найдена
        with open('bakery.csv', 'a', encoding='utf-8') as save_data:    # записываем новые данные в конец файла
            save_data.write(new_value + '\n')
        output = 'Строка не найдена. Данные дозаписаны в конец файла.'  # меняем резузультат работы функции
    return output                                           # возвращаем результат работы функции


if __name__ == '__main__':
    if len(argv) > 2 and argv[1].isdigit() and int(argv[1]):    # если аргументов больше двух и второй -
        result = edit(int(argv[1]), argv[2])                    # ненулевое число - отправляем их в функцию
    else:                                                       # иначе
        result = 'Введены неверные аргументы'                   # присваиваем к итогу сообщение об ошибке
    print(result)                                          # выводим отчёт
