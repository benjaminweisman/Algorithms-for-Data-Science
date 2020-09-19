# swap function for exchanging two list entries
import matplotlib.pyplot as pplot
import numpy as np
import numpy.random as nprnd
import time
import random
import scipy as sp
import math
from scipy.optimize import fsolve


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

def heapify(arr, n, i):
    
    maxi = i
    h1 = 2 * i + 1
    h2 = 2 * i + 2
  

    if h1 < n and arr[i] < arr[h1]: 
        maxi = h1
  
    if h2 < n and arr[maxi] < arr[h2]: 
        maxi = h2 
  
    if maxi != i:
        arr[i],arr[maxi] = arr[maxi],arr[i] 
  
        heapify(arr, n, maxi) 


def heapSort(arr):
    
    n = len(arr) 
  
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 

    
nums = [x for x in range(1, 1000)]



#list of N's
seq = [x for x in range(20, 801) if x % 20 == 0]

times=[]
times2=[]

new1=[]
new2=[]
timings = []
timings2=[]

#TYPE ALGORITHM HERE
algorithm = heapSort
#IF USING PAIR, TRUE
pair = False
if pair==True:
    #TYPE ALGORITHM 2 HERE
    algorithm2 = problem33
#DIMENSIONS OF ARRAY
dimensions = 1
runsize=False
runtime=True



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





def pairtimer(algo, algo2, timings, N, dim):
    R=1000
    for i in range(R):
        if dim == 2:
            rands = np.random.rand(N,10)
        else:
            rands = np.random.rand(N)
        start = time.time()
        algo(rands)
        end = time.time()
        timings.append(end-start)
        start2 = time.time()
        algo2(rands)
        end2=time.time()
        timings2.append(end2-start2)
    new1.append(sum(timings)/R)
    new2.append(sum(timings2)/R)
    

t=0
nlogtimes =[]

                     
if runtime == True:
    for i in seq:
        print("For N of" , i)
        if pair == True:
            pairtimer(algorithm,algorithm2, timings, i, dimensions)
            t=t+1
        else:
            times.append(timer(algorithm, timings, i, dimensions))
            t=t+1

        
    if pair == True:
        pplot.plot(seq, np.array(new1), label = str(algorithm))
        pplot.plot(seq, np.array(new2), label = str(algorithm2))
    else:
        for i in seq:
            nlogtimes.append(times/(i*np.log2(i)))
        pplot.plot(seq, np.array(times), label = str(algorithm))
        pplot.plot(seq, nlogtimes)


if runsize == True:
    if pair == True:
        pplot.plot(nums, algorithm(nums), label = str(algorithm))
        pplot.plot(nums, algorithm2(nums), label = str(algorithm2))
        t=t+1
    else:
        pplot.plot(nums, algorithm(nums), label = str(algorithm))
        t=t+1


pplot.legend()
pplot.show()
quit()





