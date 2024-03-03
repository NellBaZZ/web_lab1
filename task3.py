import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('store.sqlite')
cursor = conn.cursor()

# SQL-запрос
sql_query = """
SELECT b.title, a.name_author, COUNT(*) AS order_count
FROM book b
JOIN buy_book bb ON b.book_id = bb.book_id
JOIN buy b2 ON bb.buy_id = b2.buy_id
JOIN author a ON b.author_id = a.author_id
GROUP BY b.title, a.name_author
ORDER BY order_count DESC
LIMIT 1;
"""

# Выполнение запроса
cursor.execute(sql_query)

# Извлечение результата
result = cursor.fetchone()

# Вывод результата
if result:
    title, author, order_count = result
    print(f"Самая популярная книга: {title} (автор: {author}), заказана {order_count} раз")
else:
    print("База данных пуста или нет заказов.")

# Закрытие соединения с базой данных
conn.close()