"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
    (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
    Получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
    Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
    Найти IP адрес спамера и количество отправленных им запросов.
"""
