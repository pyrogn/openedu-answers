lletters = []
lwords = []
clines = 0
with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\5input.txt', 'r') as f:
    for line in f:
        clines += 1
        for i in line.split():
            if i.isalpha():
                lwords.append(i)
                lletters.extend(list(i))
            else:
                for j in range(len(i)):
                    if i[j].isalpha():
                        lletters.extend(i[j])
                    else:
                        i = i.replace(i[j], ' ')
                lwords.extend(i.split())
print('Input file contains:')
print(len(lletters), 'letters')
print(len(lwords), 'words')
print(clines, 'lines')
