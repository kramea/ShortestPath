# Import required modules
import networkx as nx

#Define the problem
N = nx.Graph()
X = nx.Graph()
C = nx.Graph()
B = nx.Graph()
T = nx.Graph()
#Specify weights for edges as expected mean

#Distances weightages

#N.add_weighted_edges_from([(1,2,1), (1,3,1), (1,4,1), (2,3,1),(2,4,0.5), (2,5,1),(3,4,2),(3,5,0.5),(4,5,2)])
N.add_weighted_edges_from([('FR', 'BF', 16), ('FR', 'WO', 27), ('FR', 'EM', 35), ('FR', 'DC', 43), ('FR', '12', 26), ('FR', 'RC', 38), ('DU', 'BF', 12), ('DU', 'WO', 26), ('DU', 'EM', 34), ('DU', 'DC', 42), ('RC', '12', 12), ('RC', 'WO', 12), ('RC', 'EM', 20), ('RC', 'DC', 28), ('PB', '12', 32), ('PB', 'WO', 33), ('PB', 'EM', 41), ('PB', 'DC', 49), ('DC', 'EM', 8), ('DC', 'WO', 16), ('DC', 'BF', 27), ('DC', '12', 17), ('BF', 'WO', 11), ('BF', 'EM', 19), ('BF', '12', 10), ('BF', 'RC', 22), ('WO', 'EM', 8), ('WO', '12', 1),('EM', '12', 9)])

#Find the shortest path based on the mean value of the edges
#Print shortest paths from each i to 5
X.add_weighted_edges_from([('FR', 'BF', {'dist':16, 'time':18}), ('FR', 'WO', {'dist':27, 'time':38}), ('FR', 'EM', {'dist':35, 'time':46}), ('FR', 'DC', {'dist':43, 'time':63}), ('FR', '12', {'dist':26, 'time':36}), ('FR', 'RC', {'dist':38, 'time':62}), ('DU', 'BF', {'dist':12, 'time':17}), ('DU', 'WO', {'dist':26, 'time':38}), ('DU', 'EM', {'dist':34, 'time':45}), ('DU', 'DC', {'dist':42, 'time':63}), ('RC', '12', {'dist':12, 'time':24}), ('RC', 'WO', {'dist':12, 'time':28}), ('RC', 'EM', {'dist':20, 'time':35}), ('RC', 'DC', {'dist':28, 'time':53}), ('PB', '12', {'dist':32, 'time':41}), ('PB', 'WO', {'dist':33, 'time':46}), ('PB', 'EM', {'dist':41, 'time':53}), ('PB', 'DC', {'dist':49, 'time':60}), ('DC', 'EM', {'dist':8, 'time':17}), ('DC', 'WO', {'dist':16, 'time':24}), ('DC', 'BF', {'dist':27, 'time':44}), ('DC', '12', {'dist':17, 'time':27}), ('BF', 'WO', {'dist':11, 'time':20}), ('BF', 'EM', {'dist':19, 'time':27}), ('BF', '12', {'dist':10, 'time':18}), ('BF', 'RC', {'dist':22, 'time':43}), ('WO', 'EM', {'dist':8, 'time':7}), ('WO', '12', {'dist':1, 'time':3}),('EM', '12', {'dist':9, 'time':10})])


#Time Weightages

C.add_weighted_edges_from([('FR', 'BF', {'dist':16, 'time':24}), ('FR', 'WO', {'dist':27, 'time':34}), ('FR', 'EM', {'dist':35, 'time':43}), ('FR', 'DC', {'dist':43, 'time':47}), ('FR', '12', {'dist':26, 'time':32}), ('FR', 'RC', {'dist':38, 'time':43}), ('FR', 'DU', {'dist':20, 'time':25}), ('FR', 'PB', {'dist':52, 'time':58}), ('DC', 'EM', {'dist':11, 'time':15}), ('DC', 'PB', {'dist':48, 'time':54}), ('DC', 'RC', {'dist':25, 'time':32}), ('DC', '12', {'dist':19, 'time':26}), ('DC', 'WO', {'dist':17, 'time':23}), ('DC', 'BF', {'dist':31, 'time':39}), ('DC', 'DU', {'dist':42, 'time':47}), ('DU', 'BF', {'dist':13, 'time':17}), ('DU', 'EM', {'dist':33, 'time':42}), ('DU', 'WO', {'dist':26, 'time':33}), ('DU', '12', {'dist':25, 'time':30}), ('DU', 'RC', {'dist':35, 'time':40}), ('DU', 'PB', {'dist':34, 'time':38}), ('EM', 'WO', {'dist':8, 'time':18}), ('EM', '12', {'dist':11, 'time':21}), ('EM', 'RC', {'dist':16, 'time':26}), ('EM', 'PB', {'dist':39, 'time':48}), ('EM', 'BF', {'dist':23, 'time':33}), ('PB', 'BF', {'dist':40, 'time':46}), ('PB', 'WO', {'dist':39, 'time':40}), ('PB', '12', {'dist':39, 'time':36}), ('PB', 'RC', {'dist':32, 'time':38}), ('RC', 'WO', {'dist':10, 'time':16}), ('RC', '12', {'dist':12, 'time':18}), ('RC', 'BF', {'dist':24, 'time':31}), ('WO', '12', {'dist':2, 'time':6}), ('WO', 'BF', {'dist':15, 'time':22}), ('BF', '12', {'dist':15, 'time':19})])
B.add_weighted_edges_from([('FR', 'BF', 18), ('FR', '12', 36), ('FR', 'RC', 62), ('FR', 'WO', 38), ('FR', 'EM', 46), ('FR', 'DC', 63), ('DU', 'BF', 17), ('DU', 'WO', 38), ('DU', 'EM', 45), ('DU', 'DC', 63), ('PB', '12', 41), ('PB', 'WO', 46), ('PB', 'EM', 53), ('PB', 'DC', 60), ('RC', '12', 24), ('RC', 'WO', 28), ('RC', 'EM', 35), ('RC', 'DC', 53), ('RC', 'BF', 43), ('DC', 'EM', 17), ('DC', 'WO', 24), ('DC', '12', 27), ('DC', 'BF', 44), ('EM', 'WO', 7), ('EM', '12', 10), ('EM', 'BF', 27), ('WO', '12', 3), ('WO', 'BF', 20), ('12', 'BF', 18)])
stn = N.nodes()


l = nx.shortest_path(X, 'WO', '12', weight='dist')
cl = nx.shortest_path(C, 'WO', '12', weight='dist')

btotal = 0
ctotal = 0
for k in range(len(l)):
    if k == len(l)-1:
        pass
    else:
       btotal = X.edge[l[k]][l[k+1]]['weight']['time'] + btotal

for k in range(len(cl)):
    if k == len(cl)-1:
        pass
    else:
       ctotal = C.edge[cl[k]][cl[k+1]]['weight']['time'] + ctotal       

print "Total bus time is ", btotal
print "Total car time is ", ctotal
        
#Create extra nodes in between

for m in range(len(l)-1):
    a = " "
    n = m+1           
    a = str(l[m]) + str(l[n])
    if len(l) < 5:
        X.add_edge(l[m], a, {'time':0})
        X.add_edge(a, l[n], {'time':0})
        if X.has_edge(l[m], l[n]):
            X.remove_edge(l[m], l[n])


print nx.shortest_path(X, 'WO', '12', weight='time')

    