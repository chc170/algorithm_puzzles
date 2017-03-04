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


def find_answer(state, g, i, j):

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

g = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print('9 Expected: 4.  Result: {}.'.format(answer(g)))