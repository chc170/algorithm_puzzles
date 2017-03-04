from time import time

def answer(g):
    """
    """
    rows = len(g)
    cols = len(g[0])
    
    # implemented wrong direction, so cheat here
    # transpose...
    new_g = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_g[j][i] = g[i][j]
    g = new_g
    rows, cols = cols, rows
    
    # run through all position
    state = { 0 : { 0 : 1 } }
    for i in range(rows):
        for j in range(cols):
            state = find_answer(state, g, i, j)
    # collect counts
    total = 0
    for _, state in state.items():
        for _, count in state.items():
            total += count
    return total
    
def find_answer(state, g, i, j):
    """
    """
    # state size = graph width of previous 
    #              step + 1 overlapping
    size = len(g[0]) + 2
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

    nxt_state = {}
    for fill in possible_fill_ins[g[i][j]]:
        # compose key
        if i == 0 and j == 0:
            key = 0
        elif i == 0:
            key = (fill[1][0] << 2) + (fill[0][0] << 1)
        elif j == 0:
            key = (fill[0][0] << 1) + (fill[0][1])
        else:
            key = (fill[1][0] << 2) + (fill[0][0] << 1) + (fill[0][1])

        # run through all available states
        for prev, count in state.get(key, {}).items():
            # compose new state
            part = (fill[1][0] << 2) + (fill[1][1] << 1) + (fill[0][1])
            prev = prev & ~(7 << (size - j - 3))
            new_state = (part << (size - j - 3)) | prev

            if j == (len(g[0]) - 1):
                new_state >>= 1

            # compose new key
            nxt_j = 0 if (j == len(g[0])-1) else j+1
            nxt_j = size - nxt_j - 3
            new_key = (new_state >> nxt_j) & 7

            # store new states in nxt_state
            nxt_state[new_key] = nxt_state.get(new_key, {})
            nxt_state[new_key][new_state] = nxt_state[new_key].get(new_state, 0)
            nxt_state[new_key][new_state] += count

    return nxt_state
    
    
def print_state(state):

    for k,v in state.items():
        print(' {0:03b}:'.format(k))
        for s, c in v.items():
            print('   {0:08b}: {1}'.format(s, c))



g = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print('9 Expected: 4.  Result: {}.'.format(answer(g)))

g = [
    [True, False, True, False, False, True, True, True,],
    [True, False, True, False, False, False, True, False],
    [True, True, True, False, False, False, True, False],
    [True, False, True, False, False, False, True, False],
    [True, False, True, False, False, True, True, True]
]
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
    [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True],
    [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True],
    [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True],
    [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
    [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True],
    [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
]
print('450 Expected: ?.   Result: {}.'.format(answer(g)))
