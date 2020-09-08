# swap function for exchanging two list entries
import matplotlib.pyplot as pplot
import time
import random

def Swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

#input list
A = [1,2,3,4,5,10,9,8,7,6]

for j in range(0,len(A)):
    for k in range(len(A)-1, j, -1):
        if A[k] < A[k-1]:
            Swap(A, k, k-1)


print(A)

#list of N's
seq=[10,100,1000,10000]
times=[]

#TYPE ALGORITHM HERE
algorithm = peakFinder23
dimensions = 2
print("Algorithm: ", str(algorithm))

#returns time to run algorithm in milliseconds
def timer(algo, timings, N, dim):
    R=1000
    for i in range(R):
        if dim == 2:
            rands = np.random.rand(N,10)
        else:
            rands = np.random.rand(N)
        start = time.time()
        algo(rands)
        end = time.time()
        #print((end-start)*1000)
        timings.append(end-start)
        #print(timings)
    return((sum(timings))/R)

timings = []

#To change algorithms, type algorithm here and if using 2D, change "dimensions" to 2
for i in seq:
    print("For N of" , i,": ")
    times.append(timer(algorithm, timings, i, dimensions))
    print(timer(algorithm, timings, i, dimensions), "milliseconds")
    
deltas = np.diff(times)
print("Deltas between each N")
print(deltas)
