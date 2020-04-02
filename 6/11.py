import pandas as pd
data = pd.read_csv(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\10input.csv', sep=';', encoding="windows-1251")
price = data.iloc[1, 1]
mag = ''
for i in range(len(data)):
    for j in range(1, data.shape[1]):
        if data.iloc[i, j] < price:
            price = data.iloc[i, j]
            prod = data.columns.tolist()[j]
            mag = data.iloc[i, 0]
print(f'{prod}\n{mag}')
