import pandas as pd


df = pd.read_csv('df_m5_TVI_CCI_T3_GHL.csv')
df['tradedate'] = pd.to_datetime(df['tradedate'])
df.set_index('tradedate', inplace=True)  # Индекс должен быть временной меткой

df = df.loc['2015-04-09':'2015-04-09']  # Указываем нужный диапазон дат