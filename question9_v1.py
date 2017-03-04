from time import time
from math import pow

def answer(g):

    t1 = time()
    count = 0
    rows = len(g) + 1
    cols = len(g[0]) + 1

    for val in range(int(pow(2, rows*cols))):
        state = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                state[i][j] = (val >> (i*cols + j)) % 2 == 1

        nxt = next_state(state)
        if nxt == g:
            state = [[1 if state[i][j] else 0 for j in range(cols)] for i in range(rows)]
            #print(state)
            count += 1
    print(time()-t1)
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
