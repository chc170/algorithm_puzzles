def answer(M, F):
    """
    Big number subtractions.
    """
    A = [int(d) for d in M]
    B = [int(d) for d in F]

    count = 0
    while (len(A) > 1 or A[0] > 1 or len(B) > 1 or B[0] > 1) and \
            A != [0] and B != [0]:
        A, B = subtract(A, B)
        count += 1
        
    if A == [1] and B == [1]:
        return str(count)
    return 'impossible'
    
def subtract(A, B):
    if second_is_bigger(A, B):
        A, B = B, A
    
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
        
    elif len(A) == len(B):
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            return A[i] < B[i]
    return False
    
print(answer("2", "1"))
print(answer("4", "7"))
print(answer("4", "2"))