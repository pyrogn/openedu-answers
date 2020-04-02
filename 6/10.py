import pandas as pd
data = pd.read_csv(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\10input.csv', sep=';', encoding="windows-1251")
prices = []
for i in range(len(data)):
    for j in range(1, data.shape[1]):
        prices.append(data.iloc[i, j])
print(min(prices))
