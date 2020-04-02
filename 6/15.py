import pandas as pd
df = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\15input.xlsx')
df.columns = ['x', 'y', 'z', 'k', 'l']
with open('15output.txt', 'w') as f:
    for i in df.sort_values(['y', 'x'], ascending=[False, True])['x']:
        f.write(f'{i}\n')
