from collections import Counter

f = open('collection-wordseg.txt', 'r', encoding="utf-8-sig")
wordcount = Counter(f.read().split())
f.close()

for w in wordcount.most_common(): 
    print("{}\t{}".format(*w))
