#coding:utf-8

H,W = map(int,input().rstrip().split(' '))

mirrorlist = [0 for i in range(H)]
for h in range(H):
    s = list(input())
    mirrorlist[h] = s

posx,posy=0,0 #ビームの位置
direction=0 #0：左右,1:上下
switch=1 #1:下または右,-1:上または左
count=0
while((0<=posx and posx<W) and (0<=posy and posy<H)):
    posvalue = mirrorlist[posy][posx]
    if posvalue != '_':
        #鏡がある場合は上下または左右にスイッチする
        direction = (0 if direction==1 else 1)

        if mirrorlist[posy][posx] == '/':
            #スラッシュの鏡の場合は進行方向を変える
            switch = switch * -1

    #現在地から次のマスに進む
    if direction==0:
        posx = posx + switch
    else:
        posy = posy + switch

    count+=1
print(count)
