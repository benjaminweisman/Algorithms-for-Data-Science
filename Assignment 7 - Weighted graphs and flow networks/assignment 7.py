import numpy as np
import networkx as nx
import matplotlib.pyplot as mp
import time

np.random.seed(123)
EL=[]
N=10

#EL represents edges of a directed weighted graph
#i,j,w denotes edges from vertex i to vertex j of weight w
for k in range(1,6):
    EL.append([0,k,np.random.randint(1,N)])
for k in range(1,11):
    for j in range (11,15):
        T1=np.random.randint(0,2)
        if T1==1:
            EL.append([k,j,np.random.randint(1,N)])
for k in range(11,15):
    for j in range (15,20):
        T2=np.random.randint(0,2)
        if T2==1:
            EL.append([k,j,np.random.randint(1,N)])
for k in range(15,20):
    EL.append([k,20,np.random.randint(1,N)])


#Problem 1
#Finding the adjacency Matrix
G = nx.DiGraph()
G.add_weighted_edges_from(EL)
A=nx.adjacency_matrix(G)
nx.draw_networkx(G)
mp.show()
print(A.todense())


#Problem 2
#Finding the shortest path
short = nx.dijkstra_path(G, source=0,target=20)
print("Shortest path:")
print(short)

#Finding all the shortest paths
print("Shortest paths from 0 to 20")
print([p for p in nx.all_shortest_paths(G, source=0, target=20, weight='weight')])
print("Total number of shortest paths from 0 to 20:")
print(len([p for p in nx.all_shortest_paths(G, source=0, target=20, weight='weight')]))


#Problem 3
allpaths=nx.all_simple_paths(G,source=0,target=20)
allpathslist=list(allpaths)

#crude approach but works:
paths=[]
for q in allpathslist:
    a=(list(G.get_edge_data(q[0],q[1]).values()))
    b=(list(G.get_edge_data(q[1],q[2]).values()))
    c=(list(G.get_edge_data(q[2],q[3]).values()))
    d=(list(G.get_edge_data(q[3],q[4]).values()))
    a=int(a[0])
    b=int(b[0])
    c=int(c[0])
    d=int(d[0])
    x=a*b*c*d
    paths.append(x)

rec=[]
for i in paths:
    rec.append(1/i)

largest=(max(rec))
print("Highest Probability:")
print(largest)
loc=rec.index(largest)

#Finding the path
print("Path with highest probability of success:")
print(allpathslist[loc])


#Problem 4
T=G.reverse()

G2 = G.to_undirected()
T2 = T.to_undirected()

comp=nx.compose(G2,T2)

d=nx.to_numpy_matrix(comp)
diagonal=np.diag(np.diag(d))

finaldiag= np.subtract(d,diagonal)
#print(finaldiag)

diaggraph=nx.from_numpy_matrix(finaldiag)
ece=nx.eccentricity(diaggraph)
print("Diameter:" )
print(nx.diameter(diaggraph, e=ece))


#Problem 5
print("Maximum achievable flow from source 0 to sink 20: ")
start = time.time()
print(nx.maximum_flow(G, 0, 20, capacity='weight')[0])
end = time.time()
print("Time taken:", end-start, "seconds")
