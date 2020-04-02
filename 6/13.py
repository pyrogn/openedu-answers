import pandas as pd
import zipfile

zip = zipfile.ZipFile(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\13input.zip')
list_sets = []
for i in range(1, 1001):
    zip.extract('{0}.xlsx'.format(i), path='xlsx')
    x = pd.read_excel('xlsx/{0}.xlsx'.format(i))
    list_sets.append((x.iloc[0, 1], int(x.iloc[0, 3])))
zip.close()
with open('13output.txt', 'w', encoding='utf8') as f:
    for i in sorted(list_sets):
        f.write(f'{i[0]} {i[1]}\n')
