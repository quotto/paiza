#coding:utf-8
import re

CHARACTERS = ['u','d','c','s','t','b']
N = 0

def run_characters(level,value):
    for c in CHARACTERS:
        newvalue = value + c
        if(level<N):
            run_characters(level+1,newvalue)
        else:
            if re.search(r'uud',newvalue):
                print(newvalue)

N = int(input().rstrip())
run_characters(1,'')
