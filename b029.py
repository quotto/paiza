# coding:utf-8
import math

x,y = map(int,input().rstrip().split(' '))
k = int(input())
N = int(input())
knownlist = [0 for i in range(N)]
distancelist = [0 for i in range(N)]
for i in range(N):
    xx,yy,p = map(int,input().rstrip().split(' '))
    score = math.sqrt((x - xx)**2 + (y - yy)**2)
    distancelist[i] = (i,score,p)

sorted_distance = sorted(distancelist,key=lambda distance: distance[1])

result = 0
for i in range(k):
    result += sorted_distance[i][2]

print(round(result/k))
