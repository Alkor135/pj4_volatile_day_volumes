import pandas as pd

with open('dates.txt', 'r') as file:
    dates_list = [line.strip() for line in file]

print(dates_list)

df = pd.read_csv('df_m5_TVI_CCI_T3_GHL.csv')
df['tradedate'] = pd.to_datetime(df['tradedate'])
df.set_index('tradedate', inplace=True)  # Индекс должен быть временной меткой

for date in dates_list:
    df_tmp = df.loc[date:date]  # Указываем нужный диапазон дат
    # print(df_tmp)
    # Запись в Excel
    df_tmp.to_excel(fr'dates_xls\{date}.xlsx')
