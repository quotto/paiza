#coding: utf-8
import math
from random import randint

def comb(calc_list, op):
    m1 = randint(0,99)
    # 足し算なら99以下,引き算なら0以上となる数字に絞る
    m2 = randint(0,(99 - m1 if op > 0 else m1))
    ret = [m1,m2]
    result = m1 + (m2*op)
    if ret in calc_list or result < 0 or result > 99:
        ret = comb(calc_list, op)
    return ret

M,N = map(int, input().rstrip().split())

calc_list = []
for m in range(0,M):
    ret = comb(calc_list, 1)
    print(str(ret[0]) + ' + ' + str(ret[1]) + ' =')
    calc_list.append(ret)

calc_list = []
for n in range(0,N):
    ret = comb(calc_list, -1)
    print(str(ret[0]) + ' - ' + str(ret[1]) + ' =')
    calc_list.append(ret)