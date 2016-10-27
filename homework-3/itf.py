import math
        
data = [
        [7, 2, 7, 7, 3], # Python
        [4, 5, 8, 2, 4], # course
        [1, 5, 0, 0, 7], # data
        [1, 3, 3, 1, 0], # learn
        [0, 1, 1, 1, 0], # advanced
        [0, 3, 0, 0, 0], # science
        [3, 0, 0, 0, 0], # spatial
        [0, 1, 2, 0, 0], # money
        [3, 0, 1, 0, 0], # code
        [0, 0, 1, 0, 2]  # programming
        ]

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = 0 if 0 == data[i][j] else math.log2(10/data[i][j])

term = ("Python", "course", "data", "learn", "advanced", "science", "spatial", "money", "code", "programming")
with open('itf-cal.csv', 'w') as answer:
    i = 0
    answer.write("term,one,two,three,four,five\n")
    for r in data:
        msg = "{},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f}\n".format(term[i], r[0], r[1], r[2], r[3], r[4])
        answer.write(msg)
        i += 1
answer.close()
