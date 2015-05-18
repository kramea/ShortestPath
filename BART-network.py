# Import required modules
import networkx as nx

#Define the problem
N = nx.Graph()
X = nx.Graph()
#Specify weights for edges as expected mean

#N.add_weighted_edges_from([(1,2,1), (1,3,1), (1,4,1), (2,3,1),(2,4,0.5), (2,5,1),(3,4,2),(3,5,0.5),(4,5,2)])
N.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 28), ('FR', 'EM', 36), ('FR', 'DC', 39), ('FR', '12', 26), ('FR', 'MC', 28), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 33), ('DU', 'DC', 42), ('RC', 'MC', 10), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 17), ('RC', 'DC', 25), ('PB', 'MC', 30), ('PB', '12', 32), ('PB', 'WO', 34), ('PB', 'EM', 39), ('PB', 'DC', 48), ('DC', 'EM', 11), ('DC', 'WO', 17), ('DC', 'BF', 32), ('DC', 'MC', 21), ('DC', '12', 19), ('BF', 'WO', 15), ('BF', 'EM', 23), ('BF', '12', 13), ('BF', 'MC', 15), ('BF', 'RC', 24), ('WO', 'EM', 8), ('WO', '12', 2), ('WO', 'MC', 4), ('EM', 'MC', 12),('EM', '12', 10), ('12', 'MC', 2)])

#Find the shortest path based on the mean value of the edges
#Print shortest paths from each i to 5
X.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 28), ('FR', 'EM', 36), ('FR', 'DC', 39), ('FR', '12', 26), ('FR', 'MC', 28), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 33), ('DU', 'DC', 42), ('RC', 'MC', 9), ('RC', '12', 11), ('RC', 'WO', 12), ('RC', 'EM', 17), ('RC', 'DC', 25), ('PB', 'MC', 30), ('PB', '12', 32), ('PB', 'WO', 34), ('PB', 'EM', 39), ('PB', 'DC', 48), ('DC', 'EM', 11), ('DC', 'WO', 17), ('DC', 'BF', 32), ('DC', 'MC', 21), ('DC', '12', 19), ('BF', 'WO', 14), ('BF', 'EM', 23), ('BF', '12', 13), ('BF', 'MC', 15), ('BF', 'RC', 24), ('WO', 'EM', 8), ('WO', '12', 2), ('WO', 'MC', 4), ('EM', 'MC', 12),('EM', '12', 10), ('12', 'MC', 2)])


stn = N.nodes()

for station in stn:
    for k in range(len(stn)):
        i = stn[k]
        d = nx.astar_path(N, i, station)
        for m in range(len(d)-1):
            l = " "
            n = m+1
            l = str(d[m]) + str(d[n])
            if len(l) < 5:
                X.add_path([d[m], l], weight = 0)
                X.add_path([l, d[n]], weight = 0)
            #if X.has_edge(d[m], d[n]):
                #X.remove_edge(d[m], d[n])   
            
for k in range(len(stn)):
    i = stn[k]
    d = nx.astar_path(X, i, 'DU')
    print d


    