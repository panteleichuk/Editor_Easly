from itertools import groupby

listt = [
    [2,1,0,1,2,2,2],
    [0,1,1,1,2,0,4],
    [0,2,0,1,3,0,2],
    [0,1,0,2,2,2,2],
]
for row in listt:
    for i, j in groupby(row):
        print(i, list(j))
col1 =list( zip(*listt))
print(col1)