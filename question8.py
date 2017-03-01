import math
MAX_POW = 30
MAX = math.pow(2, MAX_POW)

def answer(banana_list):
    #: initialize adjacency list
    graph = [[] for _ in range(len(banana_list))]
    for i in range(len(banana_list)-1):
        for j in range(i+1, len(banana_list)):
            if not will_end(banana_list[i], banana_list[j]):
                graph[i].append(j)
                graph[j].append(i)

    #: degrees of each point
    degs = [len(adj) for adj in graph]
    
    """
    In each iteration, remove node with least edges.
    If there is a `previous node`, that means this
    node is paired up the previous node. 
    We only count when we remove a node without
    edges and previous node.
    """
    # count single points
    count = 0
    prev = None
    idx = argmin(degs)

    while idx is not None:
        if degs[idx] == 0:
            # lonely single node
            if prev is None:
                count += 1
            degs[idx] = MAX
            idx = argmin(degs)
            prev = None
        else:
            # find neighbor with smallest degree
            ngbrs = graph[idx]
            n_degs = [degs[n] for n in ngbrs]
            n_idx = argmin(n_degs)
            nxt = ngbrs[n_idx]
            
            # udpate neighbors
            for ngbr in graph[idx]:
                degs[ngbr] -= 1
                graph[ngbr].remove(idx)
                
            # update current node
            graph[idx] = []
            degs[idx] = MAX
            
            # define next
            if prev is not None:
                idx = argmin(degs)
                prev = None
            else:
                prev = idx
                idx = nxt
                
    return count
    
def argmin(array):
    """
    Returns an index of the array that holds the
    minimum number.
    """
    min_val = MAX
    min_idx = None
    
    for i in range(len(array)):
        if array[i] < min_val:
            min_val = array[i]
            min_idx = i
            
    return min_idx
    
def will_end(a, b):
    """
    Actually play the game, but with upper bound.
    No combination will converge more than MAX_POW 
    steps.
    
    When you list first several end results (same
    numbers) and run the game backwards, you will
    figure out: if your input number is at most
    2^x you won't go any further than x steps from
    the end result. Each step will do the following
    thing:
    1. Pick one of the two numbers.
    2. Divide it by 2.
    3. Add the divided number to the other one.
    4. Repeat 1-3 until the numbers are odd.
    
    There are 2^x different possible proportions
    of the two numbers that can end the game, so
    it's more efficient to actually run the game
    rather than check the possible proportions.
    """
    count = 0
    visited = set()
    
    while a != b and count <= MAX_POW:
        # move bigger one to a
        a, b = (b, a) if a < b else (a, b)
        if (a, b) in visited:
            break
        
        visited.add((a, b))
        a, b = a-b, b+b
        count += 1
        
    return a == b
    
    
    
def will_end2(prop_dict, a, b):
    """
    """
    if a == b:
        return True

    a, b = (b, a) if a < b else (a, b)
        
    if (a+b) % 4 == 0:
        key = round(a/b, 13)
        prop = prop_dict.get(key)
        if prop and (a / prop[0] == b / prop[1]):
            return True

    return False

def _all_possible_proportions():
    """
    """
    curr = 1
    mul2 = 2
    nums = []
    while mul2 <= MAX:                                                                     
        curr = mul2 - curr
        nums.append(curr)
        mul2 *= 2

    prop_dict = {
        round(nums[i]/nums[i-1], 13):(nums[i], nums[i-1]) 
        for i in range(1, len(nums))
    }
    return prop_dict
    
# test cases
#print(len(_all_possible_proportions()))
#print(answer([1, 7, 3, 21, 13, 19]))
#print(answer([11184811, 22369621]))

# test proportion coverage
prop_dict = _all_possible_proportions()
props = [prop for _, prop in prop_dict.items()]
#for prop in props:
#    print(prop)
#    print(will_end(prop_dict, prop[0], prop[1]))
#    print(will_end2(prop[0], prop[1]))



