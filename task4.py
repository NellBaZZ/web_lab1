import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('store.sqlite')
cursor = conn.cursor()
# Создание таблицы good_order
cursor.execute('DROP TABLE IF EXISTS good_order;')
cursor.execute('CREATE TABLE IF NOT EXISTS good_order (book_id INTEGER, title VARCHAR(50), author_name VARCHAR(50));')

# SQL-запрос для вставки данных в таблицу good_order
sql_query = """
INSERT INTO good_order (book_id, title, author_name)
SELECT b.book_id, b.title, a.name_author
FROM book b
JOIN author a ON b.author_id = a.author_id
WHERE (b.amount < 5) OR ((SELECT COUNT(*) FROM buy_book bb WHERE bb.book_id = b.book_id) > 2 AND b.amount <= (SELECT AVG(amount) FROM book));
"""

# Выполнение запроса
cursor.execute(sql_query)

# Подтверждение изменений в базе данных
conn.commit()

# Закрытие соединения с базой данных
conn.close()