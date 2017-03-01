def answer(l):
    """
    Dynamic programming 
    """
    divide_count = [0] * len(l)
    count = 0
    
    # check ends at k
    for k in range(1, len(l)):
        # check j in the middle
        for j in range(k):
            if l[k] % l[j] == 0:
                divide_count[k] += 1
                # There are `divide_count[j]` numbers in front
                # of j that divides j and j divides k.
                # Therefore, there are `divide_count[j]` ways
                # to form a lucky triple that go through j
                # and ends k.
                count += divide_count[j]
    return count

def answer_keep_index(l):
    """
    sigh... i thought we exclude the duplicated lucky triples
    """
    if len(l) < 3:
        return 0
        
    muls = [[] for _ in range(len(l))]
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                muls[i].append(j)
    count = 0
    for i in range(len(l)-2):
        for j in muls[i]:
            count += len(muls[j])
    return count
    
def answer_no_duplicates(l):

    if len(l) < 3:
        return 0
    
    # O(n^2)
    muls = [[] for _ in range(len(l))]
    for i in range(len(l)-1):
        checked = set()
        for j in range(i+1, len(l)):
            if l[j] >= l[i] and l[j] % l[i] == 0 and \
                l[j] not in checked:
                checked.add(l[j])
                muls[i].append(j)
                
    # O(n^2)
    count = 0
    checked = set()
    for i in range(len(l)-2):
        # avoid duplicates
        if l[i] in checked:
            continue
        checked.add(l[i])
        for j in muls[i]:
            count += len(muls[j])
    return count

print(answer([1, 1, 1, 1, 1]))#, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
#print(answer([1, 2, 3, 4, 5, 6]))
print(answer ([2, 3, 6, 8, 5, 455, 45 ,6 , 6, 85, 16, 62, 66]))
#print(answer([3, 6, 5, 30, 18]))

