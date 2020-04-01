with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\4input.txt', 'r') as f:
    a = f.readlines()
[print(i, end='') for i in a[::-1]]
