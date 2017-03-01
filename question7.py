def answer(entrances, exits, path):
    """
    MaxFlow problem
    """
    MAX = 2000001
    rows = len(path) + 2
    cols = len(path) + 2
    
    #: capacity, flow
    capa = [[0 for _ in range(cols)] for _ in range(rows)]
    flow = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(len(path)):
        for j in range(len(path)):
            capa[i][j] = path[i][j]
    
    # add extra single source(-2) and destination(-1)
    for s in entrances:
        capa[-2][s] = MAX
    for d in exits:
        capa[d][-1] = MAX
        
    s = rows - 2
    t = rows - 1
    
    #: variables to hold augmenting path info
    args = {
        'node_to' : None,
        'visited' : None
    }
    
    total = 0
    while(has_augmenting_path(capa, flow, s, t, args)):
        # compute bottleneck capacity
        bottleneck = MAX
        v = t
        while v != s:
            u = args['node_to'][v]
            value = capa[u][v] or flow[v][u]
            bottleneck = min(bottleneck, value)
            v = u
            
        # update capacity and flow values
        v = t
        while v != s:
            u = args['node_to'][v]
            if capa[u][v] >= bottleneck:
                capa[u][v] -= bottleneck
                flow[u][v] += bottleneck
            else:
                flow[v][u] -= bottleneck
                capa[v][u] += bottleneck
            v = u
            
        # accumulating the flow of found paths
        total += bottleneck
    return total
    
    
def has_augmenting_path(capa, flow, s, t, args):
    """
    Use BFS to find augmenting path.
    """
    #: track the previous node in the path
    args['node_to'] = [0 for _ in range(len(capa))]
    #: mark the node if it's visited
    args['visited'] = [0 for _ in range(len(capa))]
    
    # initialize the queue
    queue = [s]
    args['visited'][s] = 1
    
    while queue:
        v = queue.pop(0)
        
        # find possible next nodes for v
        nxt_nodes = [u for u in range(len(capa)) 
                     if capa[v][u] > 0]
        nxt_nodes.extend(
            [u for u in range(len(capa))
             if flow[u][v] > 0])
             
        # mark unvisited next node to be visited
        # track `node_to` variable
        for u in nxt_nodes:
            if args['visited'][u] == 0:
                args['node_to'][u] = v
                args['visited'][u] = 1
                queue.append(u)
    return args['visited'][t]
    
    
    
    
    
entrances = [0, 1]
exits = [4, 5]
path = [
    [0, 0, 4, 6, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 6, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(answer(entrances, exits, path))

entrances = [0]
exits = [3]
path = [
    [0, 7, 0, 0],
    [0, 0, 6, 0],
    [0, 0, 0, 8],
    [9, 0, 0, 0]
]
print(answer(entrances, exits, path))

    