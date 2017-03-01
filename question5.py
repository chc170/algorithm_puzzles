from pprint import pprint as pp

def answer(maze):
    """
    """
    # build a matrix to store distance from the entrance
    MAX = 1000
    h = len(maze)
    w = len(maze[0])
    dist = [[MAX for _ in range(w)] for _ in range(h)]
    dist_re = [[MAX for _ in range(w)] for _ in range(h)]
    dist[0][0] = 1

    # find shortest path without remodeling
    queue = [(0, 0)]
    while queue:
        #print('Dist:')
        #pp(dist)
        #print('Re:')
        #pp(dist_re)

        cell = queue.pop(0)
        neighbors = [
            (cell[0] - 1, cell[1]),
            (cell[0], cell[1] - 1),
            (cell[0] + 1, cell[1]),
            (cell[0], cell[1] + 1)
        ]
        #: shortest distance from entrance without remodeling
        nxt_dist = dist[cell[0]][cell[1]] + 1
        #: shortest distance from entrance with remodeling
        nxt_dist_re = dist_re[cell[0]][cell[1]] + 1
        
        for n in neighbors:
            # check boundaries
            if n[0] >= 0 and n[0] < h and \
               n[1] >= 0 and n[1] < w:

                deadend = True

                # current cell is passable
                if maze[cell[0]][cell[1]] == 0:
                    # neighbor is passable and update distance without remodeling
                    if maze[n[0]][n[1]] == 0 and dist[n[0]][n[1]] > nxt_dist:
                        dist[n[0]][n[1]] = nxt_dist
                        deadend = False
                    # neighbor is passable and update distance with remodeling
                    if maze[n[0]][n[1]] == 0 and dist_re[n[0]][n[1]] > nxt_dist_re:
                        dist_re[n[0]][n[1]] = nxt_dist_re
                        deadend = False
                    # neighbor is a wall and MUST only update distance with remodeling
                    if maze[n[0]][n[1]] == 1 and dist_re[n[0]][n[1]] > nxt_dist:
                        dist_re[n[0]][n[1]] = nxt_dist
                        deadend = False

                # current cell is a wall
                else:
                    # only passable neighbor can be updated
                    # and only distance with remodeling can be updated
                    if maze[n[0]][n[1]] == 0 and dist_re[n[0]][n[1]] > nxt_dist_re:
                        dist_re[n[0]][n[1]] = nxt_dist_re
                        deadend = False

                if not deadend:
                    queue.append(n)

    return min(dist[h-1][w-1], dist_re[h-1][w-1])


print(answer([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]]))
print(answer([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
    ]))

print(answer([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0]
    ]))