# swap function for exchanging two list entries
import matplotlib.pyplot as pplot
import numpy as np
import numpy.random as nprnd
import time
import random

#input list
A = [1,2,3,4,5,10,9,8,7,6]

def Swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def script(arr):
    for j in range(0,len(arr)):
        for k in range(len(arr)-1, j, -1):
            if arr[k] < arr[k-1]:
                Swap(arr, k, k-1)
    return arr


print(A)


#list of N's
seq = [x for x in range(20, 801) if x % 20 == 0]
times=[]

#TYPE ALGORITHM HERE
algorithm = script
dimensions = 1
print("Algorithm: ", str(algorithm))

#returns time to run algorithm in milliseconds
def timer(algo, timings, N, dim):
    R=1
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

for i in seq:
    print("For N of" , i,": ")
    times.append(timer(algorithm, timings, i, dimensions))
    print(timer(algorithm, timings, i, dimensions), "milliseconds")

pplot.plot(seq, np.array(times), label = str(algorithm))
deltas = np.diff(times)
print("Deltas between each N")
print(deltas)
pplot.show()

quit()
