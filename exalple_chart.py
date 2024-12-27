import mplfinance as mpf
import pandas as pd

# Пример данных
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Open': [99, 101, 100, 102, 104, 103, 105, 107, 106, 109],
    'High': [101, 103, 102, 104, 106, 105, 107, 109, 108, 111],
    'Low': [98, 100, 99, 101, 103, 102, 104, 106, 105, 108],
    'Close': [100, 102, 101, 103, 105, 104, 106, 108, 107, 110],
    'Volume': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)  # Индекс должен быть временной меткой

# График с индикаторами
mpf.plot(
    df, 
    type='candle', 
    style='charles', 
    title='Candlestick Chart with Indicators',
    ylabel='Price',
    volume=True,
    mav=(3, 6)  # Добавляем скользящие средние
)
