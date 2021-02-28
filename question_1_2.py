"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
    (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
    Получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
    Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
    Найти IP адрес спамера и количество отправленных им запросов.
"""
request_list = []
remote_dict = {}
spam_addr = ''
spam_req_score = 0

with open('nginx_logs.txt') as f:
    for line in f:
        remote_addr = line.split()[0]
        request_type = line.split('"')[1].split()[0]
        requested_resource = line.split('"')[1].split()[1]
        request_list.append((remote_addr, request_type, requested_resource))
        remote_dict[remote_addr] = remote_dict.setdefault(remote_addr, 0) + 1
        if remote_dict[remote_addr] > spam_req_score:
            spam_addr = remote_addr
            spam_req_score = remote_dict[remote_addr]
        print(request_list[-1])

print(f'С IP {spam_addr} было совершено запросов: {spam_req_score}!')
