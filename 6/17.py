import pandas as pd
df1 = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\17input.xlsx')
df1.columns = ['x', 'kal', 'prot', 'fat', 'carbo']
df1.fillna(0, inplace=True)
df2 = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\17input.xlsx', sheet_name='Раскладка')
dic_ans = {'kal': 0, 'prot': 0, 'fat': 0, 'carbo': 0}
dic_keys = ['kal', 'prot', 'fat', 'carbo']
for day in range(1, 10):
    dic_ans = {'kal': 0, 'prot': 0, 'fat': 0, 'carbo': 0}
    for ind in range(len(df2[df2.iloc[:, 0] == day])):
        name = df2[df2.iloc[:, 0] == day].iloc[ind, 1]
        mass = float(df2[df2.iloc[:, 0] == day].iloc[ind, 2])
        for i in dic_keys:
            dic_ans[i] += float(df1[df1.x == name][i]) * mass / 100
    string = str()
    for i in dic_ans.values():
        string = string + ' ' + str(int(i))
    print(string.strip())
