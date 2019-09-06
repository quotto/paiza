# coding:utf-8

H,W,N = map(int,input().rstrip().split(' '))

fieldlist = [[0 for j in range(W)] for i in range(H)]

for i in range(N):
    h,w,x = map(int,input().rstrip().split(' '))
    # ブロック底辺の次の行から最下部までループ
    conflict = False
    #ブロックの底辺の次の行hから底辺にぶつかるまで走査
    for fh in range(h,H):
        conflict = False
        #ブロックの左端xから右端x+wまで走査
        for fw in range(x,x+w):
            #1で埋まっていたらそのひとつ上の行（fh-1）からブロックの上端fh-hまでの
            #ブロックの左端xから右端x+wを1で埋める
            if fieldlist[fh][fw]:
                conflict = True
                for hh in range(fh-h,fh):
                    for ww in range(x,x+w):
                        fieldlist[hh][ww] = 1
                break
        #ぶつかっていたら次のブロックへ
        if conflict:
            break

    if not conflict:
        # ぶつからないままループから出たら底辺に置く
        for hh in range(H-h,H):
            for ww in range(x,x+w):
                fieldlist[hh][ww] = 1

#結果の出力
for hblock in fieldlist:
    hblockresult = ''
    for wblock in hblock:
        hblockresult += ('.' if wblock==0 else '#')
    print(hblockresult)
