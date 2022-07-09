import pandas as pd


item = '/home/al/Documents/pypro/alpha_bot/lib/NAME.csv'
df = pd.read_csv(item, sep=';', comment='#', encoding='cp1251', header=None)

print(df[1])