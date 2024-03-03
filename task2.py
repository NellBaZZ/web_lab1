import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('store.sqlite')
cursor = conn.cursor()

# SQL-запрос
sql_query = """
SELECT bs.buy_id, 
       CASE 
           WHEN bs.date_step_end IS NULL THEN 'Доставлен'
           ELSE s.name_step 
       END AS step
FROM buy_step bs
LEFT JOIN step s ON bs.step_id = s.step_id
ORDER BY bs.buy_id;
"""

# Выполнение запроса
cursor.execute(sql_query)

# Извлечение результатов
results = cursor.fetchall()

# Вывод результатов
for result in results:
    buy_id, step = result
    print(f"Заказ №{buy_id}: {step}")

# Закрытие соединения с базой данных
conn.close()