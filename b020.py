#coding:utf-8
import re

N = int(input())

history = []
goto_pattern = r'go to (.+)'
back_pattern = r'use the back button'
index = 0
queries = []
for i in range(N):
    queries.append(input().rstrip())
for query in queries: 
    m = re.match(goto_pattern, query)
    if m:
        history.append(m.group(1))
        print(m.group(1))
    else:
        history.pop()
        print(history[len(history)-1])
