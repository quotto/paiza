#coding:utf-8
import re

N = int(input().rstrip())

p1 = re.compile(r's$|sh$|ch$|o$|x$')
p2 = re.compile(r'f$')
p3 = re.compile(r'fe$')
p4 = re.compile(r'y$')
p5 = re.compile(r'a|i|u|e|o')

outputlist = ['' for i in range(N)]

for i in range(N):
    word = input().rstrip()
    result = word
    if p1.search(word):
        result = word+"es"
    elif p2.search(word):
        result = word[:len(word)-1] + "ves"
    elif p3.search(word):
        result = word[:len(word)-2] + "ves"
    elif (p4.search(word)) and (len(word) > 1) and (not p5.search(word[len(word)-2])):
        result = word[:len(word)-1] + "ies"
    else:
        result = word + "s"

    outputlist[i] = result

for output in outputlist:
    print(output)
