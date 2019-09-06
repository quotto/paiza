# coding:utf-8

input_lines = str(input())
s = map(int,input_lines.rstrip().split(' '))

H,W,N = s

cardlist = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    input_lines = str(input())
    s = input_lines.rstrip().split(' ')
    for j in range(W):
        cardlist[i][j] = int(s[j])

L = int(input())
record = [0 for i in range(L)]
for i in range(L):
    input_lines = str(input())
    s = input_lines.rstrip().split(' ')
    record[i] = [[int(s[0])-1,int(s[1])-1],[int(s[2])-1,int(s[3])-1]]

result = [0] * N
current_user = 0

for r in record:
    first = cardlist[r[0][0]][r[0][1]]
    second = cardlist[r[1][0]][r[1][1]]
    if first == second:
        result[current_user] += 2
    else:
        current_user = 0 if current_user == (N - 1) else current_user+1

for score in result:
    print(score)
