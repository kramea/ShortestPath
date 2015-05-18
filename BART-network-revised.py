# Import required modules
import networkx as nx

#Define the problem
N = nx.Graph()
X = nx.Graph()
#Specify weights for edges as expected mean

#N.add_weighted_edges_from([(1,2,1), (1,3,1), (1,4,1), (2,3,1),(2,4,0.5), (2,5,1),(3,4,2),(3,5,0.5),(4,5,2)])
N.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 27), ('FR', 'EM', 35), ('FR', 'DC', 43), ('FR', '12', 26), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 34), ('DU', 'DC', 42), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 20), ('RC', 'DC', 28), ('PB', '12', 32), ('PB', 'WO', 33), ('PB', 'EM', 41), ('PB', 'DC', 49), ('DC', 'EM', 8), ('DC', 'WO', 16), ('DC', 'BF', 27), ('DC', '12', 17), ('BF', 'WO', 11), ('BF', 'EM', 19), ('BF', '12', 10), ('BF', 'RC', 22), ('WO', 'EM', 8), ('WO', '12', 1),('EM', '12', 9)])

#Find the shortest path based on the mean value of the edges
#Print shortest paths from each i to 5
X.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 27), ('FR', 'EM', 35), ('FR', 'DC', 43), ('FR', '12', 26), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 34), ('DU', 'DC', 42), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 20), ('RC', 'DC', 28), ('PB', '12', 32), ('PB', 'WO', 33), ('PB', 'EM', 41), ('PB', 'DC', 49), ('DC', 'EM', 8), ('DC', 'WO', 16), ('DC', 'BF', 27), ('DC', '12', 17), ('BF', 'WO', 11), ('BF', 'EM', 19), ('BF', '12', 10), ('BF', 'RC', 22), ('WO', 'EM', 8), ('WO', '12', 1),('EM', '12', 9)])


stn = N.nodes()

for k in range(len(stn)):
    i = stn[k]
    d = nx.astar_path(N, i, 'FR')
    for m in range(len(d)-1):
        l = " "
        n = m+1
        l = str(d[m]) + str(d[n])
        if len(l) < 5:
            X.add_edge(d[m], l, weight = 0)
            X.add_edge(l, d[n], weight = 0)
            if X.has_edge(d[m], d[n]):
                X.remove_edge(d[m], d[n])   


            
for k in range(len(stn)):
    i = stn[k]
    d = nx.astar_path(X, i, 'FR')
    print d


    