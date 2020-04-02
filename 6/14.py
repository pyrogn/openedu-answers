import pandas as pd
import numpy as np
df = pd.read_excel(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\14input.xlsx')
dic_med = {}
for i in range(df.shape[0]):
    dic_med[df.iloc[i, 0]] = np.median(df.iloc[i, 1:df.shape[1]])
reg = max(dic_med, key=dic_med.get)
dic_prof = {}
for i in range(1, df.shape[1]):
    dic_prof[df.columns.tolist()[i]] = np.mean(df.iloc[:, i])
prof = max(dic_prof, key=dic_prof.get)
with open('14output.txt', 'w') as f:
    f.write(f'{reg} {prof}')
