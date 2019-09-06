#coding:utf-8

import calendar
import datetime

year,month = map(int,input().rstrip().split('/'))

#対象年月の最初の曜日と月末日
firstweekday,dates = calendar.monthrange(year,month)
#日曜日を0スタートにする
firstweekday = 0 if firstweekday==6 else firstweekday-1

#1週分の出力文字列
output='    '

#最初の曜日までブランクで埋める
for i in range(firstweekday):
    output+='     '

for d in range(dates):
    date=d+1
    now = datetime.datetime(year,month,date)
    weekday = now.weekday()

    #コンソール出力整形用のブランク（10日以前ならブランク2つ）
    blank = '  ' if date < 10 else ' '
    if weekday==5:
        output+="[{0}]".format(date)
        print(output)
        output=''
    elif weekday==6:
        output+="({0}){1}".format(date,blank)
    else:
        output+="{0}{1}".format(date,blank)

if len(output) > 0:
    print(output)
