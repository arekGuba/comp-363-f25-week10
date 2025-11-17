def DFS_helper(G, v, marked, topo_order):
    """
    Visits vertices, but only adds vertices to topo_order
    after all of a node's children have been visited/don't exist.
    Reversing that order in the primary method returns topo order.
    """
    # Mark the current vertex as visited
    marked.append(v)

    # Consider all the neighbors of v
    for w in range(len(G)):
        # For any edge v --> w, if w is unmarked, plan to visit it.
        if G[v][w] != G[0][0] and w not in marked:
            DFS_helper(G, w, marked, topo_order)
    
    # add vertex to topo_order after all children have been explored
    topo_order.append(v)


def DFS(G):
    N = len(G)
    marked = []
    topo_order = []

    for v in range(N):
        if v not in marked:
            DFS_helper(G, v, marked, topo_order)

    topo_order.reverse()
    return topo_order


G1 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

G2 = [
    [0,0,1,0,1,1],
    [0,0,1,0,0,0],
    [0,0,0,0,1,1],
    [0,1,2,0,0,1],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0]
]

print(DFS(G1))
