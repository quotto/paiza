#coding:utf-8

N = int(input())
result = [{'score':0,'W':0,'L':0,'D':0, 'index':n} for n in range(N)]
for n in range(N):
    query = input().rstrip()
    for i in range(n+1,len(query)):
        if query[i] == 'W':
            result[n]['score'] += 2
            result[n]['W'] += 1
            result[i]['L'] += 1
        elif query[i] == 'L':
            result[n]['L'] += 1
            result[i]['score'] += 2
            result[i]['W'] += 1
        elif query[i] == 'D':
            result[n]['score'] += 1
            result[n]['D'] += 1
            result[i]['score'] += 1
            result[i]['D'] += 1

result = sorted(result,key=lambda x:x['score'],reverse=True)
top = result[0]
print('{} {} {} {} {}'.format(top['index']+1, top['score'], top['W'], top['D'], top['L']))