from time import time

def answer(g):

    rows = len(g)
    cols = len(g[0])
    new_state = ''.join(['x'] * (cols+2))
    state = {
        'xxx' : {new_state : 1},
    }
    t1 = time()
    for i in range(rows):
        for j in range(cols):
            state = find_answer(state, g, i, j)
            n_states = 0
            for _, val in state.items():
                n_states += len(val)
            output = '# of keys: {}. # of states: {}'.format(len(state),
                                                             n_states)
            #print(output)

    print('Run time: {}'.format(time()-t1))
    #print(state)
    total = 0
    for _, state in state.items():
        for _, count in state.items():
            total += count
    return total

def find_answer(state, g, i, j):

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
    #print(state)
    nxt_state = {}
    for fill in possible_fill_ins[g[i][j]]:
        if i == 0 and j == 0:
            key = 'xxx'
        elif i == 0:
            key = str(fill[1][0]) + str(fill[0][0]) + 'x'
        elif j == 0:
            key = 'x' + str(fill[0][0]) + str(fill[0][1])
        else:
            key = str(fill[1][0]) + str(fill[0][0]) + str(fill[0][1])

        for prev, count in state.get(key, {}).items():
            part = str(fill[1][0]) + str(fill[1][1]) + str(fill[0][1])
            new_state = prev[:j] + part + prev[j+3:]
            if j == (len(g[0]) - 1):
                new_state = 'x' + new_state[:-1]

            nxt_j = 0 if (j == len(g[0])-1) else j+1
            new_key = new_state[nxt_j:nxt_j+3]
            nxt_state[new_key] = nxt_state.get(new_key, {})
            nxt_state[new_key][new_state] = nxt_state[new_key].get(new_state, 0)
            nxt_state[new_key][new_state] += count

    return nxt_state


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
#print('216 Expected: ?.   Result: {}.'.format(answer(g)))

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
#print('450 Expected: ?.   Result: {}.'.format(answer(g)))
