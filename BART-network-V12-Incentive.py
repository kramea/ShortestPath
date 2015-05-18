# Import required modules
import networkx as nx
import numpy

O = raw_input("Enter Origin Station Code")
D = raw_input("Enter Destination Station Code")
r = numpy.zeros(shape=(15,6))

#Define the problem
X = nx.Graph()
C = nx.Graph()
BTICKT = nx.Graph()

X.add_weighted_edges_from([('FR', 'BF', {'dist':16, 'time':18}), ('FR', 'WO', {'dist':27, 'time':38}), ('FR', 'EM', {'dist':35, 'time':46}), ('FR', 'DC', {'dist':43, 'time':63}), ('FR', '12', {'dist':26, 'time':36}), ('FR', 'RC', {'dist':38, 'time':62}), ('DU', 'BF', {'dist':12, 'time':17}), ('DU', 'WO', {'dist':26, 'time':38}), ('DU', 'EM', {'dist':34, 'time':45}), ('DU', 'DC', {'dist':42, 'time':63}), ('RC', '12', {'dist':12, 'time':24}), ('RC', 'WO', {'dist':12, 'time':28}), ('RC', 'EM', {'dist':20, 'time':35}), ('RC', 'DC', {'dist':28, 'time':53}), ('PB', '12', {'dist':32, 'time':41}), ('PB', 'WO', {'dist':33, 'time':46}), ('PB', 'EM', {'dist':41, 'time':53}), ('PB', 'DC', {'dist':49, 'time':60}), ('DC', 'EM', {'dist':8, 'time':17}), ('DC', 'WO', {'dist':16, 'time':24}), ('DC', 'BF', {'dist':27, 'time':44}), ('DC', '12', {'dist':17, 'time':27}), ('BF', 'WO', {'dist':11, 'time':20}), ('BF', 'EM', {'dist':19, 'time':27}), ('BF', '12', {'dist':10, 'time':18}), ('BF', 'RC', {'dist':22, 'time':43}), ('WO', 'EM', {'dist':8, 'time':7}), ('WO', '12', {'dist':1, 'time':3}),('EM', '12', {'dist':9, 'time':10})])

#Time Weightages

C.add_weighted_edges_from([('FR', 'BF', {'dist':16, 'time':24}), ('FR', 'WO', {'dist':27, 'time':34}), ('FR', 'EM', {'dist':35, 'time':43}), ('FR', 'DC', {'dist':43, 'time':47}), ('FR', '12', {'dist':26, 'time':32}), ('FR', 'RC', {'dist':38, 'time':43}), ('FR', 'DU', {'dist':20, 'time':25}), ('FR', 'PB', {'dist':52, 'time':58}), ('DC', 'EM', {'dist':11, 'time':15}), ('DC', 'PB', {'dist':48, 'time':54}), ('DC', 'RC', {'dist':25, 'time':32}), ('DC', '12', {'dist':19, 'time':26}), ('DC', 'WO', {'dist':17, 'time':23}), ('DC', 'BF', {'dist':31, 'time':39}), ('DC', 'DU', {'dist':42, 'time':47}), ('DU', 'BF', {'dist':13, 'time':17}), ('DU', 'EM', {'dist':33, 'time':42}), ('DU', 'WO', {'dist':26, 'time':33}), ('DU', '12', {'dist':25, 'time':30}), ('DU', 'RC', {'dist':35, 'time':40}), ('DU', 'PB', {'dist':34, 'time':38}), ('EM', 'WO', {'dist':8, 'time':18}), ('EM', '12', {'dist':11, 'time':21}), ('EM', 'RC', {'dist':16, 'time':26}), ('EM', 'PB', {'dist':39, 'time':48}), ('EM', 'BF', {'dist':23, 'time':33}), ('PB', 'BF', {'dist':40, 'time':46}), ('PB', 'WO', {'dist':39, 'time':40}), ('PB', '12', {'dist':39, 'time':36}), ('PB', 'RC', {'dist':32, 'time':38}), ('RC', 'WO', {'dist':10, 'time':16}), ('RC', '12', {'dist':12, 'time':18}), ('RC', 'BF', {'dist':24, 'time':31}), ('WO', '12', {'dist':2, 'time':6}), ('WO', 'BF', {'dist':15, 'time':22}), ('BF', '12', {'dist':15, 'time':19})])

BTICKT.add_weighted_edges_from([('FR', 'BF', 1.75), ('FR', 'WO', 4.10), ('FR', 'EM', 5.60), ('FR', 'DC', 6.00), ('FR', '12', 4.00), ('FR', 'RC', 4.85), ('FR', 'DU', 4.35), ('FR', 'PB', 6.40), ('DC', 'EM', 2.95), ('DC', 'PB', 6.35), ('DC', 'RC', 4.65), ('DC', '12', 3.80), ('DC', 'WO', 3.75), ('DC', 'BF', 4.75), ('DC', 'DU', 6.00), ('DU', 'BF', 1.75), ('DU', 'EM', 5.55), ('DU', 'WO', 4.10), ('DU', '12', 4.00), ('DU', 'RC', 4.85), ('DU', 'PB', 6.35), ('EM', 'WO', 2.90), ('EM', '12', 3.10), ('EM', 'RC', 4.25), ('EM', 'PB', 5.95), ('EM', 'BF', 4.30), ('PB', 'BF', 5.10), ('PB', 'WO', 4.45), ('PB', '12', 4.30), ('PB', 'RC', 4.90), ('RC', 'WO', 2.75), ('RC', '12', 2.60), ('RC', 'BF', 3.60), ('WO', '12', 1.75), ('WO', 'BF', 2.75), ('BF', '12', 2.60)])

def original_path(origin, destination):
    w = nx.shortest_path(X, origin, destination, weight='dist')
    distance = []    
    for wnode in range(len(w)-1):
        distance.append(X.edge[w[wnode]][w[wnode+1]]['weight']['time'])
    return distance                        

def find_path(origin,destination):
    l = nx.shortest_path(X, origin, destination, weight='dist')
    cl = nx.shortest_path(C, origin, destination, weight='dist')    
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
    return nx.shortest_path(X, origin, destination, weight='time')

pdistance = original_path(O, D)
ppath = find_path(O, D)

if len(ppath) == 3:
    if ppath[0] == 'DC': # Daly City *********************************************************
        if ppath[2] == 'EM' or ppath[2] == 'WO':
            X.node['DC']['stime'] = 1
            dclist = []
            for t in range(1,60,15):
                newt = t
                dclist.append(newt)
                newt = newt + 5
                dclist.append(newt)
                newt = newt + 3
                dclist.append(newt)
                newt = newt+ 4
                dclist.append(newt)
        if ppath[2] == 'DU':
            X.node['DC']['stime'] = 6
            dclist = []
            for t in range(6,60,15):
                dclist.append(t)
        if ppath[2] == 'FR':
            X.node['DC']['stime'] = 13
            dclist=[]
            for t in range(13,60,15):
                dclist.append(t)
        if ppath[2] == 'PB':
            X.node['DC']['stime'] = 9
            dclist=[]
            for t in range(9,60,15):
                dclist.append(t)
        if ppath[2] == 'RC':
            X.node['DC']['stime'] = 1
            dclist = []
            for t in range(1,60,15):
                dclist.append(t)
        if ppath[2] == '12':
            X.node['DC']['stime']=1
            dclist = []
            for t in range(1,60,15):
                newt = t
                dclist.append(newt)
                newt = newt + 8
                dclist.append(newt)
        if ppath[2] == 'BF':
            X.node['DC']['stime'] = 6
            dclist = []
            for t in range(6,60,15):
                newt = t
                dclist.append(newt)
                newt = newt + 7
                dclist.append(newt)
            
    if ppath[0] == 'EM': # Embarcadero ********************************************************
        if ppath[2] == 'DC':
            X.node['EM']['stime'] = 2
            emlist = []
            for t in range(2,60,15):
                newt = t
                emlist.append(newt)
                newt = newt + 3
                emlist.append(newt)
                newt = newt + 2
                emlist.append(newt)
                newt = newt + 6
                emlist.append(newt)
        if ppath[2] == 'WO':
            X.node['EM']['stime'] = 0
            emlist = []
            for t in range(0,60,15):
                newt = t
                emlist.append(newt)
                newt = newt + 3
                emlist.append(newt)
                newt = newt + 5
                emlist.append(newt)
                newt = newt + 3
                emlist.append(newt)
        if ppath[2] == 'DU':
            X.node['EM']['stime'] = 9
            emlist = []
            for t in range(9,60,15):
                emlist.append(t)
        if ppath[2] == 'FR':
            X.node['EM']['stime'] = 0
            emlist = []
            for t in range(0,60,15):
                emlist.append(t)
        if ppath[2] == 'PB':
            X.node['EM']['stime'] = 11
            emlist = []
            for t in range(11,60,15):
                emlist.append(t)
        if ppath[2] == 'RC':
            X.node['EM']['stime'] = 3
            emlist = []
            for t in range(3,60,15):
                emlist.append(t)
        if ppath[2] == 'BF':
            X.node['EM']['stime'] = 0
            emlist = []
            for t in range(0,60,15):
                newt = t
                emlist.append(newt)
                newt = newt + 8
                emlist.append(newt)
        if ppath[2] == '12':
            X.node['EM']['stime'] = 3
            emlist = []
            for t in range(3,60,15):
                newt = t
                emlist.append(newt)
                newt = newt + 8
                emlist.append(newt)
                        
    if ppath[0] == 'WO': # West Oakland *************************************************
        if ppath[2] == 'DC' or ppath[2] == 'EM':
            X.node['WO']['stime'] = 6
            wolist = []
            for t in range(6,60,15):
                newt = t
                wolist.append(newt)
                newt = newt + 4
                wolist.append(newt)
                newt = newt + 3
                wolist.append(newt)
                newt = newt + 1
                wolist.append(newt)
        if ppath[2] == 'BF':
            X.node['WO']['stime'] = 0
            wolist = []
            for t in range(0,60,15):
                newt = t
                wolist.append(newt)
                newt = newt + 7
                wolist.append(newt)
        if ppath[2] == 'FR':
            X.node['WO']['stime'] = 7
            wolist = []
            for t in range(7,60,15):
                wolist.append(t)

        if ppath[2] == 'DU':
            X.node['DU']['stime'] = 0
            wolist = []
            for t in range(0,60,15):
                wolist.append(t)
        if ppath[2] == '12':
            X.node['WO']['stime'] = 3
            wolist = []
            for t in range(3,60,15):
                newt = t
                wolist.append(newt)
                newt = newt + 7
                wolist.append(newt)
        if ppath[2] == 'RC':
            X.node['WO']['stime'] = 10
            wolist = []
            for t in range(10,60,15):
                wolist.append(t)
        if ppath[2] == 'PB':
            X.node['WO']['stime'] = 3
            wolist = []
            for t in range(3,60,15):
                wolist.append(t)
                
    if ppath[0] == '12': #12th Street Oakland *************************************************
        if ppath[2] == 'BF' or ppath[2] == 'FR':
            X.node['12']['stime'] = 0
            twlist = []
            for t in range(0,60,15):
                twlist.append(t)
        if ppath[2] == 'DC' or ppath[2] == 'EM' or ppath[2] == 'WO': 
            X.node['12']['stime'] = 4
            twlist = []
            for t in range(6,60,15):
                if t == 6:
                    twlist.append(t)
                    newt = t
                newt = newt + 2
                twlist.append(newt)
                newt = newt + 13
                twlist.append(newt)
        if ppath[2] == 'PB':
            X.node['12']['stime'] = 6
            twlist = []
            for t in range(6,60,15):
                twlist.append(t)
        if ppath[2] == 'RC':
            X.node['12']['stime'] = 4
            twlist = []
            for t in range(6,60,15):
                if t == 6:
                    twlist.append(t)
                    newt = t
                newt = newt + 7
                twlist.append(newt)
                newt = newt + 8
                twlist.append(newt)
    if ppath[0] == 'PB': #Pittsburg **********************************************************
        pblist = []
        if ppath[2] == 'DC' or ppath[2] == '12' or ppath[2] == 'EM' or ppath[2] == 'WO':
            X.node['PB']['start'] = 2
            X.node['PB']['interval'] = 15
            #pblist = []
            for t in range(2,60,15):
                pblist.append(t)
    if ppath[0] == 'DU': #Dublin *************************************************************
        dulist = []
        if ppath[2] == 'DC' or ppath[2] == 'BF' or ppath[2] == 'WO' or ppath[2] == 'EM':
            X.node['DU']['stime'] = 13
            X.node['DU']['interval'] = 15
            for t in range(13,60,15):
                dulist.append(t)
    if ppath[0] == 'FR': #Fremont Station ****************************************************
        if ppath[2] == 'DC' or ppath[2] == 'EM' or ppath[2] == 'WO':
            X.node['FR']['stime'] = 6
            X.node['FR']['interval'] = 15
            frlist = []
            for t in range(6, 60, 15):
                frlist.append(t)
        if ppath[2] == 'RC' or ppath[2] == '12':
            X.node['FR']['stime'] = 0
            X.node['FR']['interval'] = 15
            frlist = []
            for t in range(0,60,15):
                frlist.append(t)
        if ppath[2] == 'BF':
            X.node['FR']['stime'] = 0
            frlist = []
            for t in range(0,60,15):
                if t == 0:
                    frlist.append(t)
                    newt = t
                newt = newt + 6
                frlist.append(newt)
                newt = newt + 9
                frlist.append(newt)
    if ppath[0] == 'RC': #Richmond Station ************************************************
        if ppath[2] == 'FR' or ppath[2] == 'BF':
            X.node['RC']['stime'] = 5
            X.node['RC']['interval'] = 15
            rclist = []
            for t in range(5,60,15):
                rclist.append(t)
        if ppath[2] == 'DC' or ppath[2] == 'EM' or ppath[2] == 'WO':
            X.node['RC']['stime'] = 12
            X.node['RC']['interval'] = 15
            rclist = []
            for t in range(12,60,15):
                rclist.append(t)
        if ppath[2] == '12':
            X.node['RC']['stime'] = 5
            rclist = []
            for t in range(0,60,15):
                if t == 5:
                    rclist.append(t)
                    newt = t
                newt = newt + 7
                rclist.append(newt)
                newt = newt + 3
                rclist.append(newt)
    if ppath[0] == 'BF': #Bay Fair ********************************************************
        if ppath[2] == 'DU':
            X.node['BF']['stime'] = 5
            X.node['BF']['interval'] = 15
            bflist = []
            for t in range(5,60,15):
                bflist.append(t)
        if ppath[2] == 'FR':
            X.node['BF']['stime'] = 3
            X.node['BF']['interval'] = 15
            bflist = []
            for t in range(5,60,15):
                bflist.append(t)
        if ppath[2] == 'RC' or ppath[2] == '12':
            X.node['BF']['stime'] = 3
            X.node['BF']['interval'] = 15
            bflist = []
            for t in range(5,60,15):
                bflist.append(t)
        if ppath[2] == 'DC' or ppath[2] == 'EM' or ppath[2] == 'WO':
            X.node['BF']['stime'] = 0
            X.node['BF']['interval'] = 15
            bflist = []
            for t in range(5,60,15):
                bflist.append(t)

if len(ppath) > 4:
    if ppath[0] == 'RC': #Richmond*********************************************************
        if ppath[2] == '12':
            X.node['RC']['stime'] = 5
            rclist = []
            for t in range(0,60,15):
                if t == 5:
                    rclist.append(t)
                    newt = t
                newt = newt + 7
                rclist.append(newt)
                newt = newt + 3
                rclist.append(newt)
            if ppath[4] == 'PB':
                X.node['12']['stime'] = 6
                X.node['12']['interval'] = 15
                twlist = []
                for t in range(6,60,15):
                    twlist.append(t)
        if ppath[2] == 'BF':
            X.node['RC']['stime'] = 5
            X.node['RC']['interval'] = 15
            rclist = []
            for t in range(5,60,15):
                rclist.append(t)
            if ppath[4] == 'DU':
                X.node['BF']['stime'] = 5
                X.node['BF']['interval'] = 15
                bflist = []
                for t in range(5,60,15):
                    bflist.append(t)

    if ppath[0] == 'PB': #Pittsburg **********************************************************
        pblist = []
        if ppath[2] == '12':
            X.node['PB']['stime'] = 2
            #pblist = []
            for t in range(2,60,15):
                pblist.append(t)
            if ppath[4] == 'RC':
                X.node['12']['stime'] = 4
                twlist = []
                for t in range(6,60,15):
                    newt = t
                    twlist.append(newt)
                    newt = newt + 7
                    twlist.append(newt)
            if ppath[4] == 'FR' or ppath[4] == 'BF':
                X.node['12']['stime'] = 0
                twlist = []
                for t in range(0,60,15):
                    twlist.append(t)
                if len(ppath) > 5:
                    if ppath[6] == 'DU':
                        X.node['BF']['stime'] == 5
                        bflist = []
                        for t in range(5,60,15):
                            bflist.append(t)
            

    if ppath[0] == 'BF': #Bay Fair ************************************************************
        if ppath[2] == '12':
            X.node['BF']['stime'] = 3
            bflist = []
            for t in range(3,60,15):
                bflist.append(t)
            if ppath[4] == 'PB':
                X.node['12']['stime'] = 6
                twlist = []
                for t in range(6,60,15):
                    twlist.append(t)

    if ppath[0] == 'DU': # Dublin *************************************************************
        dulist = []
        if ppath[2] == 'BF':
            X.node['DU']['stime'] = 13
            #dulist = []
            for t in range(13,60,15):
                dulist.append(t)
            if ppath[4] == 'RC': 
                X.node['BF']['stime'] = 3
                bflist = []
                for t in range(3,60,15):
                    bflist.append(t)
            if ppath[4] == 'FR':
                X.node['BF']['stime'] = 3
                bflist = []
                for t in range(3,60,15):
                    bflist.append(t)
            if ppath[4] == '12':
                X.node['BF']['stime'] = 3
                bflist = []
                for t in range(3,60,15):
                    bflist.append(t)
                if len(ppath) > 5:
                    if ppath[6] == 'PB':
                        X.node['12']['stime'] = 6
                        twlist = []
                        for t in range(6,60,15):
                            twlist.append(t) 
                
    if ppath[0] == 'FR': #Fremont**************************************************************
        if ppath[2] == 'BF':
            X.node['FR']['stime'] = 0
            frlist = []
            for t in range(0,60,15):
                if t == 0:
                    frlist.append(t)
                    newt = t
                newt = newt + 6
                frlist.append(newt)
                newt = newt + 9
                frlist.append(newt)
            if ppath[4] == 'DU':
                X.node['BF']['stime'] = 5
                X.node['BF']['interval'] = 15
                bflist = []
                for t in range(5,60,15):
                    bflist.append(t)
        if ppath[2] == 'WO':
            X.node['FR']['stime'] = 6
            X.node['FR']['interval'] = 15
            frlist = []
            for t in range(6, 60, 15):
                frlist.append(t)
            if ppath[4] == 'PB':
                X.node['WO']['stime'] = 3
                X.node['WO']['interval'] = 15
                wolist = []
                for t in range(3, 60, 15):
                    wolist.append(t)                     
        if ppath[2] == '12':
            X.node['FR']['stime'] = 0
            X.node['FR']['interval'] = 15
            frlist = []
            for t in range(0,60,15):
                frlist.append(t)
            if ppath[4] == 'PB':
                X.node['12']['stime'] = 6
                X.node['12']['interval'] = 15
                twlist = []
                for t in range(6, 60, 15):
                    twlist.append(t)
    
xlist = []
ylist = []
zlist = []
if ppath[0] == 'FR':
    xlist = frlist
if ppath[0] == 'RC':
    xlist = rclist
if ppath[0] == 'DC':
    xlist = dclist
if ppath[0] == 'EM':
    xlist = emlist
if ppath[0] == 'WO':
    xlist = wolist
if ppath[0] == '12':
    xlist = twlist
if ppath[0] == 'BF':
    xlist = bflist
if ppath[0] == 'DU':
    xlist = dulist
if ppath[0] == 'PB':
    xlist = pblist

if len(ppath) > 3:
    if ppath[2] == 'BF':
        ylist = bflist
    if ppath[2] == '12':
        ylist = twlist
    if ppath[2] == 'WO':
        ylist = wolist

if len(ppath) > 5:
    if ppath[4] == '12':
        zlist = twlist
    if ppath[4] == 'BF':
        zlist = bflist
    if ppath[4] == 'WO':
        zlist = wolist

for start in range(0,15,1):  
    for time in xlist:
        if start > time:
            pass
        if start <= time:
            delay = time - start
            break
        
    if len(ppath) > 3:
        midtime = pdistance[0]
        totaldist = delay + midtime
        for time in ylist:
            if midtime > time:
                pass
            if midtime <= time:
                delay2 = time - midtime
                break
    else:
        totaldist = pdistance[0] + delay
            
    if len(ppath) > 3:    
        totaldist = delay2 + totaldist + pdistance[1]

    cartime = C.edge[O][D]['weight']['time']
    cardist = C.edge[O][D]['weight']['dist']

    #calculate travel cost (include ticket fare, value of time for income groups, parking and toll costs for SF destinations)
    #Include wear and tear cost, price of car + insurance etc. in the cost of driving

    #VOT

    vot = numpy.array([2.87, 7.45, 12.84, 20.58, 44.17, 74.92])
    parking = 15
    toll = 5
    oakpark = 12

    ctime_cost = vot * cartime
    btime_cost = vot * totaldist
    carp_time = numpy.zeros(6)
    cp_cost = (cartime*0.15)
    for i in range(len(ctime_cost)):
        carp_time[i] = ctime_cost[i] + cp_cost
        cp_cost = cp_cost + (cartime*0.15)

    carfuel = ((4.0/30)*cardist) + (cardist*(0.7))
    if D == 'EM':
        carfuel = parking + carfuel
        if O != 'DC':
            carfuel = carfuel + toll

    carp_fuel = (((4.0/30)*cardist) + (cardist*(0.7)))/3
    if D == 'EM':
        carp_fuel = parking/3 + carp_fuel
        if O != 'DC':
            carp_fuel = carp_fuel + 2.50

    if D == '12':
        carfuel = oakpark + carfuel
        carp_fuel = oakpark/3 + carp_fuel


    bart_cost = btime_cost 
    car_cost = ctime_cost + carfuel
    carp_cost = carp_time + carp_fuel

    for i in range(len(vot)):
        if car_cost[i] < bart_cost[i] and car_cost[i] < carp_cost[i]:
            r[start,i] = 1
        elif bart_cost[i] < car_cost[i] and bart_cost[i] < carp_cost[i]:
            r[start,i] = 2
        elif carp_cost[i] < car_cost[i] and carp_cost[i] < bart_cost[i]:
            r[start,i] = 3

    #print carfuel, ctime_cost
    #print BTICKT.edge[O][D]['weight'], btime_cost


opmode = []
for col in range(0,15):
    opmode.append([])
    for row in range(0,6):
        if r[col, row] == 1:
            opmode[col].append('CAR')
        if r[col,row] == 2:
            opmode[col].append('BART')
        if r[col,row] == 3:
            opmode[col].append('Carpool')



for col in range(0,15):
    print opmode[col] 

"""
file = "C:\\mode.txt"
numpy.savetxt(file,r)"""