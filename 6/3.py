dic = {}
with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\3input.txt', 'r') as f:
    allwords = f.read().split()
    for word in set(allwords):
        dic[word] = allwords.count(word)

with open('3output.txt', 'w') as w:
    for i in [v[0] for v in sorted(dic.items(), key=lambda kv: (-kv[1], kv[0]))]:
        w.write(i + ' ')
