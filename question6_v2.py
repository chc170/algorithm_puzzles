def answer(M, F):
    """
    Big number subtractions : too slow.
    Big number divisions
    """
    A = [int(d) for d in M]
    B = [int(d) for d in F]

    # keep dividing the bigger number by the smaller number
    # until one of the numbers is 0 or 1
    count = 0
    while A != [0] and B != [0] and A != [1] and B != [1]:
        if second_is_bigger(A, B):
            A, B = B, A
        res, remain = divide(A, B)
        A, B = B, remain
        count += res
        
    if A != [0] and B != [0] and (A == [1] or B == [1]):
        if second_is_bigger(A, B):
            A, B = B, A
            
        # calculate the difference between the results
        _, A = subtract(A, B)
        B = [int(d) for d in str(count)]

        # add the difference to the count
        carry = 0
        result = ''
        for i in range(1, max(len(A), len(B))+1):
            iA = 0 if i > len(A) else A[-i]
            iB = 0 if i > len(B) else B[-i]
            
            d = iA + iB + carry
            carry = d // 10
            d = d % 10
            
            result = str(d) + result
        return result
    return 'impossible'
    
def divide(A, B):
    
    count = 0
    idx = 1
    tmp = [A[0]]
    while idx < len(A):
        if second_is_bigger(tmp, B):
            tmp.append(A[idx])
            idx += 1
            count *= 10

        while second_is_bigger(B, tmp):
            _, tmp = subtract(tmp, B)
            count += 1

    while second_is_bigger(B, tmp):
        _, tmp = subtract(tmp, B)
        count += 1
    return count, tmp
    
def subtract(A, B):
    
    diff = []
    carry = 0
    for i in range(1, len(A)+1):
        iA = A[-i]
        iB = 0 if i > len(B) else B[-i]
        
        d = iA - iB - carry
        if d < 0:
            carry = 1
            d += 10
        else:
            carry = 0
        
        diff.insert(0, d)
    
    while len(diff) > 1 and diff[0] == 0:
        diff.pop(0)
    return B, diff
    
def second_is_bigger(A, B):
    if len(A) < len(B):
        return True
    elif len(A) > len(B):
        return False
    elif len(A) == len(B):
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            return A[i] < B[i]
    return True
    
print(answer('1', '1111111111111111'))
print(answer("1", "1"))
print(answer("2", "1"))
print(answer("4", "7"))
print(answer("4", "2"))
print(answer("4245234523452352345", "2687567276354625"))