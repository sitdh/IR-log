import glob, os
from nltk.corpus import stopwords
from collections import Counter

os.chdir('documents/raw')

all_terms = list()
stopword = stopwords.words('english')

for f in glob.glob('*.txt'):
    with open(f, 'r') as data:
        msg = [d for d in data.read().replace("\n", '').split() if d not in stopword]
        all_terms += list(msg)
        cnt = Counter(msg).most_common()
        
        ordered = open('../../documents/ordered/' + f, 'a')
        for k in cnt:
            ordered.write("%s,%s\n" % k)
        ordered.close()


    data.close()

all_terms = [a for a in all_terms if a not in stopword]
cnd = Counter(all_terms).most_common()
os.chdir('../..')
with open('documents/ordered/msg-rank.txt', 'a') as rank:
    for k in cnd:
        rank.write("%s,%s\n" % k)

rank.close()
