import pandas as pd
data = pd.read_csv(
    r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\9input.csv', sep=';', header=None)
data = data[[1, 0]]
data.to_csv('9output.csv', index=False, header=None, sep=';')
