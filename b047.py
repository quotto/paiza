#coding: utf-8

type_str = input()
left_hand = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v','b']]
right_hand = [['y','u','i','o','p'],['h','j','k','l'],['n','m']]

prev_row = 0
prev_col = 0
count = 0
current_hand = 0 #1:左 2:右
for s in type_str:
    for i in range(0,3):
        if s in left_hand[i]:
            row = i
            col = left_hand[i].index(s)+1
            diff_col = abs(prev_col - col)
            diff_row = abs(prev_row - row)
            if(((diff_col <= 1 and diff_row == 0) or (diff_col ==0 and diff_row ==1))and current_hand == 2):
                count += 1
            else: current_hand = 1
            prev_col = col
            prev_row = row
            break
        
        if s in right_hand[i]:
            row = i
            col = len(left_hand[i]) + right_hand[i].index(s)+1
            diff_col = abs(prev_col - col)
            diff_row = abs(prev_row - row)
            if(((diff_col <= 1 and diff_row == 0) or (diff_col ==0 and diff_row ==1))and current_hand == 1):
                count += 1
            else: current_hand = 2
            prev_col = col
            prev_row = row
            break

print(count)

    