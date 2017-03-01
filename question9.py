from math import pow

def answer(g):
    #check = [[None for _ in range(len(g[0]))] for _ in range(len(g))]
    #for i in range(len(g)):
    #    for j in range(len(g[0])):
    #        # must be 1
    #        if i > 0 and j > 0 and (g[i][j] + g[i-1][j] + g[i][j-1] + g[i-1][j-1]) > 2:
    #            check[i][j] = 1
    #        # must be 0
    #        elif (i+1 < len(g) and (g[i][j] + g[i+1][j]) == 2) or \
    #             (j+1 < len(g[0]) and (g[i][j] + g[i][j+1]) == 2):
    #             check[i][j] = 0

    #g = [[True, False], [False, True]]
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
            print(state)
            count += 1
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
    [True, False],
    [True, True] 
]
print('Expected: 4.  Result: {}.'.format(answer(g)))

g = [[True, False, True, False, False, True, True, True],
     [True, False, True, False, False, False, True, False],
     [True, True, True, False, False, False, True, False],
     [True, False, True, False, False, False, True, False],
     [True, False, True, False, False, True, True, True]]
#print('Expected: 254.   Result: {}.'.format(answer(g)))




