#coding:utf-8

CHARACTERS = ['u','d','c','s','t','b']
N = 3

def run_characters(level,value):
    for c in CHARACTERS:
        newvalue = value + c
        if(level<N):
            run_characters(level+1,newvalue)
        else:
            print(newvalue)

run_characters(1,'')
