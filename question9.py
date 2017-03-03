from math import pow
from time import time

cache = {}

def answer(g):
    global cache
    cache = {}
    ######
    rows = len(g)
    cols = len(g[0])
    check = [[None for _ in range(cols + 1)] for _ in range(rows + 1)]
    t1 = time()
    count = find_answer(check, g, 0, 0)
    print('Run time: {}'.format(time()-t1))
    return count
    print('Result1: {}.'.format(count))


    ######
    #t1 = time()
    #count = 0
    #rows = len(g) + 1
    #cols = len(g[0]) + 1

    #for val in range(int(pow(2, rows*cols))):
    #    state = [[0 for _ in range(cols)] for _ in range(rows)]
    #    for i in range(rows):
    #        for j in range(cols):
    #            state[i][j] = (val >> (i*cols + j)) % 2 == 1

    #    nxt = next_state(state)
    #    if nxt == g:
    #        state = [[1 if state[i][j] else 0 for j in range(cols)] for i in range(rows)]
    #        #print(state)
    #        count += 1
    #print(time()-t1)
    #print('Result2: {}.'.format(count))

    
def find_answer_(state, g, i, j):

    if i == len(g):
        return 1
    
    global cache
    key = None


    nxt_j = j + 1 if (j+1) < len(g[0]) else 0
    nxt_i = i + 1 if nxt_j == 0 else i
    
    possible_fill_ins = {
        False : [
            [[1, 1], [0, 0]],
            [[1, 0], [1, 0]],
            [[1, 0], [0, 1]],
            [[0, 1], [1, 0]],
            [[0, 1], [0, 1]],
            [[0, 0], [1, 1]],
            [[1, 1], [1, 0]],
            [[1, 1], [0, 1]],
            [[1, 0], [1, 1]],
            [[0, 1], [1, 1]],
            [[1, 1], [1, 1]],
            [[0, 0], [0, 0]],
        ],
        True : [
            [[0, 0], [0, 1]],
            [[0, 0], [1, 0]],
            [[0, 1], [0, 0]],
            [[1, 0], [0, 0]],
        ]
    }
    
    count = 0
    for fill in possible_fill_ins[g[i][j]]:
        if i == 0 and j == 0:
            state[i][j]   = fill[0][0]

        if i == 0:
            state[i][j+1] = fill[0][1]

        if j == 0: 
            state[i+1][j] = fill[1][0]

        if state[i][j] != fill[0][0] or \
           state[i][j+1] != fill[0][1] or \
           state[i+1][j] != fill[1][0]:
            continue

        state[i+1][j+1] = fill[1][1] 

        key = ''
        for idx in range(len(state[0])):
            if idx <= j:
                key += str(state[i+1][idx])
            else:
                key += str(state[i][idx])
        key = (key, i, j, fill[1][1])
        if key in cache:
            cnt = cache[key]
        else:
            cnt = find_answer(state, g, nxt_i, nxt_j)
            cache[key] = cnt
        count += cnt
    return count

def next_state(state):
    rows = len(state) - 1
    cols = len(state[0]) - 1
    nxt = [[False for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            nxt[i][j] = (state[i][j] + state[i+1][j] + state[i][j+1] + state[i+1][j+1]) == 1
    return nxt

g = [
    [True, False, True],
    [False, True, False],
    [True, False, True] 
]

print('9 Expected: 4.  Result: {}.'.format(answer(g)))

g = [[True, False, True, False, False, True, True, True,],
     [True, False, True, False, False, False, True, False],
     [True, True, True, False, False, False, True, False],
     [True, False, True, False, False, False, True, False],
     [True, False, True, False, False, True, True, True]]
print('40 Expected: 254.   Result: {}.'.format(answer(g)))

g = [
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False],
]
print('108 Expected: ?.   Result: {}.'.format(answer(g)))

g = [
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, True, False],
]
print('216 Expected: ?.   Result: {}.'.format(answer(g)))

g = [
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
[True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, True, False, False, True, True, True, True, True],
]
print('450 Expected: ?.   Result: {}.'.format(answer(g)))


