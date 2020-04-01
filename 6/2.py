with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\2input.txt', 'r') as f:
    for line in f:
        print(sum(map(int, line.split())), end=' ')
