import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('store.sqlite')
cursor = conn.cursor()

# SQL-запрос
sql_query = """
WITH ranked_books AS (
    SELECT
        ROW_NUMBER() OVER (PARTITION BY a.name_author ORDER BY b.amount) AS 'Nпп',
        a.name_author AS Автор,
        CASE
            WHEN LENGTH(b.title) > 15 THEN SUBSTR(b.title, 1, 12) || '...'
            ELSE b.title
        END AS Книга,
        b.amount AS 'Кол-во',
        RANK() OVER (PARTITION BY a.name_author ORDER BY b.title desc) AS 'Ранг',
        SUM(b.amount) OVER (PARTITION BY a.name_author) AS 'Распределение',
        ROUND(((b.amount * 100)) / (SUM(b.amount) OVER (PARTITION BY a.name_author)), 2) / 100 AS 'Ранг,%'
    FROM author a
    JOIN book b ON a.author_id = b.author_id
    WHERE a.name_author IN ('Булгаков М.А.', 'Пушкин А.С.', 'Лермонтов М.Ю.')
    )
SELECT * FROM ranked_books
ORDER BY 'Автор', 'Кол-во';
"""

# Выполнение запроса
cursor.execute(sql_query)

# Извлечение результатов
results = cursor.fetchall()
print("|  Nпп  |  Автор  |  Книга  |  Количество  |  Ранг  |  Распределение  |  Ранг,%  |")
# Вывод результатов
for result in results:
    print(result)

# Закрытие соединения с базой данных
conn.close()