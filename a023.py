#coding: utf-8

N = int(input())
S = list(map(int, input().rstrip().split(' ')))

rest_day = 0
count = 0
max_count = 0
for i in range(7):
    if S[i] == 0: rest_day+=1

if rest_day >= 2: count = 7

#休日の合計が2日以下なら無条件に0日
for j in range(1,N-6):
    if S[j-1] == 0: rest_day-=1
    if S[j+6] == 0: rest_day+=1
    if(rest_day >= 2):
        count = 7 if count < 7 else count+1
    else:
        max_count = count if count > max_count else max_count
        count = 0

max_count = count if count > max_count else max_count
print(max_count)