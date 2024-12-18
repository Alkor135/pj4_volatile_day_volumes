import sqlite3
import pandas as pd

# Установить соединение с базой данных
conn = sqlite3.connect(r'C:\Users\Alkor\gd\data_quote_db\RTS_futures_minute.db')

# SQL-запрос для извлечения данных
query = "SELECT * FROM Minute"  # Замените table_name на имя вашей таблицы

# Загрузить данные в DataFrame
df = pd.read_sql_query(query, conn)

# Закрыть соединение
conn.close()

# Показать первые несколько строк DataFrame
# print(df)

df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE'])

# Добавление колонки с датой
df['date'] = df['TRADEDATE'].dt.date

# Вычисление накопленных объемов по дням
df['daily_cumulative_volume'] = df.groupby('date')['VOLUME'].cumsum()

print(df)
