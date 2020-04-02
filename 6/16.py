import pandas as pd
df1 = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\16input.xlsx')
df1.columns = ['x', 'kal', 'prot', 'fat', 'carbo']
df1.fillna(0, inplace=True)
df2 = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\16input.xlsx', sheet_name='Раскладка')
dic_ans = {'kal': 0, 'prot': 0, 'fat': 0, 'carbo': 0}
dic_keys = ['kal', 'prot', 'fat', 'carbo']
for ind in range(len(df2.iloc[:, 0])):
    name = df2.iloc[ind, 0]
    mass = float(df2.iloc[ind, 1])
    for i in dic_keys:
        dic_ans[i] += float(df1[df1.x == name][i]) * mass / 100
for i in dic_ans.values():
    print(int(i), end=' ')
