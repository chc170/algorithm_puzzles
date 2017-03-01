def answer(l, t):
    # check standards
    if len(l) < 1 or len(l) > 100:
        return [-1, -1]
    if l[0] < 1 or l[0] > 100:
        return [-1, -1]
    if t < 0 or t > 250:
        return [-1, -1]
    
    # run two pointers to indicates the start 
    # and end positions
    ptr1 = 0
    ptr2 = 1
    sub_sum = l[0]
    
    while ptr1 < len(l) or ptr2 < len(l):
        if sub_sum == t:
            break
        
        if sub_sum < t:
            if ptr2 >= len(l) or l[ptr2] > 100 or l[ptr2] < 1:
                return [-1, -1]
                
            sub_sum += l[ptr2]
            ptr2 += 1
        else:
            sub_sum -= l[ptr1]
            ptr1 += 1
            
    if sub_sum == t:
        return [ptr1, ptr2-1]
    return [-1, -1]


print(answer([4,3,10,2,8], 12))
print(answer([1,2,3,4], 15))