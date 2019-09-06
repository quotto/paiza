# coding:utf-8
import math

def calcpos(direction,c,m,lim):
    c += (m * d)
    if(c >= lim):
        param = math.floor(c / lim)
        c = c - (lim * param)
    elif(c < 0):
        param = math.ceil(abs(c) / lim)
        c = (lim * param) + c
    return c

w,h,n = map(int,input().rstrip().split(' '))
x,y = map(int,input().rstrip().split(' '))
for i in range(n):
    loglist = input().rstrip().split(' ')

    d = 1 # 加算/減算の識別子
    if(loglist[0] == "L" or loglist[0] == "D"):
        #下か左への移動なら減算
        d = -1

    if(loglist[0] == "U" or loglist[0] == "D"):
        y = calcpos(d,y,int(loglist[1]),h)
    else:
        x = calcpos(d,x,int(loglist[1]),w)

print(str(x) + " " + str(y))
