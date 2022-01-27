import networkx as nx


def make_nx_graph(graph):
    G = nx.Graph()
    for i,j in enumerate(graph):
        G.add_node(i)
        for x,z in enumerate(j[0]):
            G.add_edge(i, z, weight=j[1][x])
    return G


if __name__ == "__main__":


    import time
    from graphs import *
    
    
    strt = 0
    end = 29
    
    T = make_nx_graph(graph2)
    order,result = nx.dijkstra_predecessor_and_distance(T, strt)
    point = end
    order_list = [0]
    while point != strt:
        order_list.insert(1, point)
        point = order.get(point)[0]

    start = time.time()
    for x in range(10000):
        nx.dijkstra_predecessor_and_distance(T, strt)
    time = (time.time() - start) / 10000

    print("Time: %gsec" %time)
    print("Order: %s" %"->".join([str(i) for i in order_list]))
    print("Shortest path lenght: %i" %result.get(end))
