import pandas as pd
import jieba
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_excel(f"G:\泰迪\附件1\酒店评论.xlsx"))
arr = data["评论内容"]
words = []
for i in range(arr.size):
    words.append(jieba.lcut(arr[i]))
counts = {}
wfile = open(r'G:\result.txt','w')
s = [line.strip() for line in open(r"G:\stop_word.txt",encoding="utf-8").readlines()]

for i in range(len(words)):
    for word in words[i]:
        if word not in s:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
    wfile.write(word + ',' + str(count) + '\n')
