import pandas as pd
import mplfinance as mpf

df = pd.read_csv('df_m5_TVI_CCI_T3_GHL.csv')
df['tradedate'] = pd.to_datetime(df['tradedate'])
df.set_index('tradedate', inplace=True)  # Индекс должен быть временной меткой

df = df.loc['2015-04-09':'2015-04-09']  # Указываем нужный диапазон дат

print(df)

# График с индикаторами
mpf.plot(
    df, 
    type='candle', 
    style='charles', 
    title='Candlestick Chart with Indicators',
    ylabel='Price',
    # volume=True,
    volume=False
    # mav=(3, 6)  # Добавляем скользящие средние
)
