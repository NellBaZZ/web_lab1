import sqlite3

# Подключение к базе данных
con = sqlite3.connect('store.sqlite')
cursor = con.cursor()

# SQL-запрос
sql_query = """
SELECT c.name_city, bs.buy_id
FROM city c
JOIN client cl ON c.city_id = cl.city_id
JOIN buy b ON cl.client_id = b.client_id
JOIN buy_step bs ON b.buy_id = bs.buy_id
JOIN step s ON bs.step_id = s.step_id
WHERE s.name_step = 'Транспортировка'
ORDER BY c.name_city, bs.buy_id;
"""

# Выполнение запроса
cursor.execute(sql_query)

# Извлечение результатов
results = cursor.fetchall()

# Вывод результатов
for result in results:
    city_name, buy_id = result
    print(f"Заказ №{buy_id} направлен в город {city_name}")

# Закрытие соединения с базой данных
con.close()