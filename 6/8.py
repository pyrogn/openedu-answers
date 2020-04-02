# я датасаентист, мне можно
import pandas as pd
data = pd.read_csv(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\8input.csv', sep=';', header=None)
ans = data.groupby(0).mean().sort_values(1)
for i in ans.index:
    print(i)
