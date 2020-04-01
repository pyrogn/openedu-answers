# здесь уже близко. но я устал.
lletters = []
lwords = []
clines = 0
with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\5input.txt', 'r') as f:
    for line in f:
        clines += 1
        for i in line.split():
            if i.isalpha:
                lwords.append(i)
                lletters.extend(list(i))
print(clines)
print(len(lwords))
print(len(lletters))
