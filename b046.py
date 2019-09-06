# coding:utf-8
import math

ED = {"E":0,"N":1,"S":1,"W":2}
WD = {"W":0,"N":1,"S":1,"E":0}
SD = {"S":0,"N":0,"E":1,"W":2}
ND = {"N":0,"S":0,"E":1,"W":2}

DISTANCE = {"E":ED,"W":WD,"S":SD,"N":ND}

N = int(input())
source = input().rstrip().split(' ')
dest = input().rstrip().split(' ')

# 方角が同じ場合は直線距離が最短
d = DISTANCE[source[1]][dest[1]]
s = source[0] - dest[0]
result = 0
if source[1] == dest[1]:
    result = math.fabs(source[0] - dest[0]) * 100
else:
    calcdis(source,dest,0)


def calcdis(d,s,current):
    # 目的地に着いたらリターン
    if(d == 0 and s == 0):
        return result
    # 方角が同じであれば直進
    elif(d == 0 and s > 0):
        s -= 1
        new_value = current + 100
        return calcdis(new_value)
    # 同心円上であれば円周を1/4進む
    elif(d > 0 and s==0):
        d -= 1
        new_value = current + ((1/2) * math.pi * 100)
        return calcdis(new_value)
    else:
        new_value = current + ((1/2) * math.pi * 100)
        calcdis(d-1,s,new_value)

        new_value = current + 100
        calcdis(d,s-1,new_value)
