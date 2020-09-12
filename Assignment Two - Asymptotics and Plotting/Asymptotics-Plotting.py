# swap function for exchanging two list entries
import matplotlib.pyplot as pplot
import numpy as np
import numpy.random as nprnd
import time
import random
import scipy as sp
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

#test these individually after writing them

def problem2a(arr):
    ar=[]
    for x in arr:  
        x=4*(x**2)+x
        ar.append(x)
    return ar

def problem2b(arr):
    ar=[]
    for x in arr:
        x=64*x * np.log2(x) + 2*x
        ar.append(x)
    return ar

#problem 2b
#gives a warning
def findIntersect(arr):
    for x in arr:
        intersect = sp.optimize.fsolve(lambda x:4*x**2+x-64*x*np.log2(x)+2*x, x)
    return intersect

nums = [x for x in range(1, 1000)]
print(findIntersect(nums))


def problem31(arr):
    ar=[]
    for x in arr:
        x=x**2
        ar.append(x)
    return ar

def problem32(arr):
    ar=[]
    for x in arr:
        x=np.sqrt(x)
        ar.append(x)
    return ar

def problem33(arr):
    ar=[]
    for x in arr:
        x=2**x
        ar.append(x)
    return ar

def problem34(arr):
    ar=[]
    for x in arr:
        x=np.log2(x)
        ar.append(x)
    return ar

def problem35(arr):
    ar=[]
    for x in arr:
        x=.5**x
        ar.append(x)
    return ar

def problem36(arr):
    ar=[]
    for x in arr:
        x=x*np.log2(x)
        ar.append(x)
    return ar

def problem37(arr):
    ar=[]
    for x in arr:
        x=x
        ar.append(x)
    return ar

def problem38(arr):
    ar=[]
    for x in arr:
        x=x**3
        ar.append(x)
    return ar 


#list of N's
seq = [x for x in range(20, 801) if x % 20 == 0]
times=[]
times2=[]

new1=[]
new2=[]
timings = []
timings2=[]

#TYPE ALGORITHM HERE
algorithm = problem38
#IF USING PAIR, TRUE
pair = True
if pair==True:
    #TYPE ALGORITHM 2 HERE
    algorithm2 = problem33
#DIMENSIONS OF ARRAY
dimensions = 1
runsize=True
runtime=False



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
        pplot.plot(seq, np.array(times), label = str(algorithm))



if runsize == True:
    if pair == True:
        pplot.plot(nums, algorithm(nums), label = str(algorithm))
        pplot.plot(nums, algorithm2(nums), label = str(algorithm2))
        t=t+1
    else:
        pplot.plot(nums, algorithm(nums), label = str(algorithm))
        t=t+1


'''
deltas = np.diff(times)
print("Deltas between each N")
print(deltas)
'''


pplot.legend()
pplot.show()
quit()





