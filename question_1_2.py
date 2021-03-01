"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
    (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
    Получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
    Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
    Найти IP адрес спамера и количество отправленных им запросов.
"""
request_list = []   # объявляем список запросов
remote_dict = {}    # объявляем словарь для списка пользователей с количествами их обращений
spam_addr = ''      # объявляем переменную для адреса спамера
spam_req_score = 0  # и переменную максимального количества запросов

with open('nginx_logs.txt', encoding='utf-8') as f:                     # открываем файл
    for line in f:                                                          # читаем его построчно
        remote_addr = line.split()[0]                                           # адрес - до первого пробела
        request_type = line.split('"')[1].split()[0]                            # тип запроса - первый после кавычек
        requested_resource = line.split('"')[1].split()[1]                      # ресурс второй после кавычек
        request_list.append((remote_addr, request_type, requested_resource))    # добавляем кортеж с данными
        print(request_list[-1])                                                 # выводим добавленный кортеж с данными
        remote_dict[remote_addr] = remote_dict.setdefault(remote_addr, 0) + 1   # пополняем словарь или поднимаем счет
        if remote_dict[remote_addr] > spam_req_score:                           # если текущий счёт больше максимального
            spam_addr = remote_addr                                                 # обновляем адрес спамера
            spam_req_score = remote_dict[remote_addr]                               # и максимальный счёт

print(f'С IP {spam_addr} было совершено запросов: {spam_req_score}!')   # выводим адрес и количество запросов спамера
