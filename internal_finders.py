import pandas as pd


item = '/home/al/Documents/pypro/alpha_bot/lib/data/NAME.csv'
df = pd.read_csv(item, sep=';', comment='#', encoding='cp1251', header=None)

data = df[1]

name_list = []
for name in data:
    name_list.append(name)

print(len(name_list))
name_str = (' ').join(name_list).replace(',', ' ')
print(name_str.find('Алексей'))
names_file_item = '/home/al/Documents/pypro/alpha_bot/lib/data/names'
with open(names_file_item, 'w') as f:
    f.write(name_str)

with open(names_file_item, 'r') as f:
    names = f.read()

print(names)