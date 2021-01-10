#coding:utf-8

def main(lines):
    query = lines.split(' ')

    target = int(query[len(query)-1])

    ans = []
    #数字と単語の組み合わせを調べつつ出力対象に格納
    for i in range(len(query)-1):
        val,word = query[i].split(':') 
        if target % int(val) == 0:
            ans.append({'key': int(val), 'word': word})

    #対象が無ければ数字をそのまま出力
    if len(ans) == 0: print(target)
    else: 
        #keyをキーとして昇順ソート後にwordを出力
        ans = sorted(ans, key=lambda x:x['key'])
        for a in ans:
            print(a['word'], end='')
    


if __name__ == '__main__':
    lines = input().rstrip()
    main(lines)
