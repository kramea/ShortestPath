# Import required modules
import networkx as nx

#Define the problem
N = nx.Graph()
X = nx.Graph()
C = nx.Graph()
B = nx.Graph()
#Specify weights for edges as expected mean

#Distances weightages

#N.add_weighted_edges_from([(1,2,1), (1,3,1), (1,4,1), (2,3,1),(2,4,0.5), (2,5,1),(3,4,2),(3,5,0.5),(4,5,2)])
N.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 27), ('FR', 'EM', 35), ('FR', 'DC', 43), ('FR', '12', 26), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 34), ('DU', 'DC', 42), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 20), ('RC', 'DC', 28), ('PB', '12', 32), ('PB', 'WO', 33), ('PB', 'EM', 41), ('PB', 'DC', 49), ('DC', 'EM', 8), ('DC', 'WO', 16), ('DC', 'BF', 27), ('DC', '12', 17), ('BF', 'WO', 11), ('BF', 'EM', 19), ('BF', '12', 10), ('BF', 'RC', 22), ('WO', 'EM', 8), ('WO', '12', 1),('EM', '12', 9)])

#Find the shortest path based on the mean value of the edges
#Print shortest paths from each i to 5
X.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 27), ('FR', 'EM', 35), ('FR', 'DC', 43), ('FR', '12', 26), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 34), ('DU', 'DC', 42), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 20), ('RC', 'DC', 28), ('PB', '12', 32), ('PB', 'WO', 33), ('PB', 'EM', 41), ('PB', 'DC', 49), ('DC', 'EM', 8), ('DC', 'WO', 16), ('DC', 'BF', 27), ('DC', '12', 17), ('BF', 'WO', 11), ('BF', 'EM', 19), ('BF', '12', 10), ('BF', 'RC', 22), ('WO', 'EM', 8), ('WO', '12', 1),('EM', '12', 9)])


#Time Weightages

C.add_weighted_edges_from([('FR', 'BF', 24), ('FR', 'WO', 34), ('FR', 'EM', 43), ('FR', 'DC', 47), ('FR', '12', 32), ('FR', 'RC', 43), ('FR', 'DU', 25), ('FR', 'PB', 58), ('DC', 'EM', 15), ('DC', 'PB', 54), ('DC', 'RC', 32), ('DC', '12', 26), ('DC', 'WO', 23), ('DC', 'BF', 39), ('DC', 'DU', 47), ('DU', 'BF', 17), ('DU', 'EM', 42), ('DU', 'WO', 33), ('DU', '12', 30), ('DU', 'RC', 40), ('DU', 'PB', 38), ('EM', 'WO', 18), ('EM', '12', 21), ('EM', 'RC', 26), ('EM', 'PB', 48), ('EM', 'BF', 33), ('PB', 'BF', 46), ('PB', 'WO', 40), ('PB', '12', 36), ('PB', 'RC', 38), ('RC', 'WO', 16), ('RC', '12', 18), ('RC', 'BF', 31), ('WO', '12', 6), ('WO', 'BF', 22), ('BF', '12', 19)])
B.add_weighted_edges_from([('FR', 'BF', 18), ('FR', '12', 36), ('FR', 'RC', 62), ('FR', 'WO', 38), ('FR', 'EM', 46), ('FR', 'DC', 63), ('DU', 'BF', 17), ('DU', 'WO', 38), ('DU', 'EM', 45), ('DU', 'DC', 63), ('PB', '12', 41), ('PB', 'WO', 46), ('PB', 'EM', 53), ('PB', 'DC', 60), ('RC', '12', 24), ('RC', 'WO', 28), ('RC', 'EM', 35), ('RC', 'DC', 53), ('RC', 'BF', 43), ('DC', 'EM', 17), ('DC', 'WO', 24), ('DC', '12', 27), ('DC', 'BF', 44), ('EM', 'WO', 7), ('EM', '12', 10), ('EM', 'BF', 27), ('WO', '12', 3), ('WO', 'BF', 20), ('12', 'BF', 18)])
stn = N.nodes()

for k in range(len(stn)):
    i = stn[k]
    d = nx.astar_path(N, i, 'FR')
    for m in range(len(d)-1):
        l = " "
        n = m+1
        l = str(d[m]) + str(d[n])
        if len(l) < 5:
            X.add_path([d[m], l], weight = 0)
            X.add_path([l, d[n]], weight = 0)
            if X.has_edge(d[m], d[n]):
                X.remove_edge(d[m], d[n])   
            
for k in range(len(stn)):
    i = stn[k]
    d = nx.astar_path(X, i, 'FR')
    print d


    