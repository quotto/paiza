#coding-utf8
import sys

def main(lines):
    N,Q = list(map(int, lines[0].split(' ')))
    age = [0 for n in range(N)]
    memo = [[-1 for n in range(N)] for n in range(N)]

    for q in (lines[1:]):
        t1,t2,diff = list(map(int,q.split()))
        age1 = age[t1-1]
        age2 = age[t2-1]

        age2 = age1 + diff
        age1 = age2 + (diff*-1)
        age[t1-1] = age1
        age[t2-1] = age2

        if diff < 0:
            memo[t1-1][t2-1] = 2 #t2はt1より小さい
            memo[t2-1][t1-1] = 1 #t1はt2より大きい
        elif diff > 0:
            memo[t1-1][t2-1] = 1 #t2はt1より大きい
            memo[t2-1][t1-1] = 2 #t1はt2より小さい
        else:
            #t1とt2は同じ
            memo[t1-1][t2-1] = 0 
            memo[t2-1][t1-1] = 0 

    for i in range(len(memo)):
       for j in range(len(memo[i])):
        if i != j:
            # iとjの関係
            itoj = memo[i][j]
            # jとkの関係
            for k in range(len(memo[j])):
                if i!=k and j!=k:
                    jtok = memo[j][k]
                    #kとiの関係
                    ktoi = memo[k][i]

                    print('i={},j={},k={}'.format(i,j,k))
                    print(itoj,jtok,ktoi)
                    #i<j,j<kでi>K
                    if itoj == 1 and jtok == 1 and ktoi == 2:
                        print("miss match")
                    # i>j,j>kでk>i
                    if itoj == 2 and jtok == 2 and ktoi == 2:
                        print("miss match")

    max_age = max(age)
    min_age = min(age) 
    if(min_age < 0):
        min_age += abs(min_age)
        max_age += abs(min_age)
    if(max_age > 100):
        max_age -= (100 - max_age)
        min_age -= (100 - max_age)

    if(max_age > 100 or min_age < 0):
        print(-1)
    else:
        print(max_age - min_age)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)