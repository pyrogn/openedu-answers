with open(r'c:\Users\Professional\Documents\GitHub\openedu-answers\6\6input.txt', 'r') as f:
    dic = {}
    for i in f.readlines():
        dic[i] = len(i)
# выводит лишь первую строку с максимальной длиной
print(max(dic, key=dic.get))
# а этот код будет выводить все строки с максимальной длиной, хотя не очень рационально.
# maxl = max(dic.values())
# for key, value in dic.items():
#     if value == maxl:
#         print(key)
