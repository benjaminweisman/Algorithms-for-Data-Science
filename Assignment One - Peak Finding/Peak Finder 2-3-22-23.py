import numpy as np
import numpy.random as nprnd
import matplotlib.pyplot as pplot
from random import randint
import time
import timeit

cnt = 0 # This is a global counter for the number of compares

def peakFinder2(ar):
    
    global cnt
    p=ar[0]
    j=1
    n=(len(ar))
    
    while (p < ar[j]) and (j < n + 1):
        cnt += 1
        p=ar[j]
        j=j+1
    cnt+=1   
    return p


def peakFinder3(arr):

    global cnt

    if len(arr) == 0:
        cnt+=1
        return None
    
    if len(arr) == 2:
        cnt+=1
        return arr[1]
    
    median = len(arr)//2

    #did not use strict inequalities so indexed a bit differently but works same
    if arr[median-1] < arr[median] and arr[median] > arr[median+1]:
        cnt += 2
        return arr[median]
    
    if arr[median-1] >= arr[median]:
        cnt += 1
        p = peakFinder3(arr[0:median])
        if p:
            return p
        
    if median >= 1 and arr[median+1] >= arr[median]:
        cnt += 2
        p = peakFinder3(arr[median:len(arr)])
        if p:
            return p


def findMax(array):
    global cnt
    maximum = array[0]
    index = 0
    
    for i in range(len(array)):
        if maximum >= array[i]:
            cnt+=1
            maximum = array[i]
            index = 1
            
    return index


#must take in numpy array
def peakFinder22(arr):
    global cnt
    i=0
    j=0
    p = arr[i][j]
    if ((p<arr[i][j-1]) or (p<arr[i][j+1]) or (p<arr[i-1][j]) or (p<arr[i+1][j])):
        cnt +=1
        p=max([arr[i][j-1],arr[i][j+1], arr[i-1][j],arr[i+1][j]])
        cnt +=1
        l=np.where(arr == p)
        k=list(zip(l[0],l[1]))
    return(p)

        
def peakFinder23(arr):
    global cnt
    if len(arr) == 0:
        cnt+=1
        return None

    if len(arr) > 1:
        cnt+=1
        if len(arr[0]) == 0:
            cnt+=1
            return None

    median = len(arr[0]) // 2

    col = [arr[i][median] for i in range(len(arr))]

    n = findMax(col)

    if len(arr[0]) == 2:
        cnt+=1
        return arr[n][median]

    if arr[n][median-1] < arr[n][median] > arr[n][median+1]:
        cnt+=2
        return arr[n][median]

    if arr[n][median-1] >= arr[n][median]:
        cnt+=1
        return peakFinder23([arr[n][:median] for n in range(len(arr))])

    if arr[n][median+1] >= arr[n][median]:
        cnt+=1
        return peakFinder23([arr[n][median:] for n in range(len(arr))])

'''
#Function to test algorithms using number of comparisons (not as consistent)
def tester(algo, timings, N, dimensions):
    global cnt
    R=1000
    for i in range(R):
        cnt=0
        if dimensions == 2:
            N=N//100
            rands = np.random.rand(N,N)
        else:
            rands = np.random.rand(N)
        algo(rands)
        timings.append(cnt)
    #print(cntlist)
    print(sum(timings))
    return((sum(timings))/R)

timings = []
print(tester(peakFinder23, timings, 500000, 2))
'''

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

if algorithm == peakFinder2:
    print("Worst complexity should be theta(N)")
if algorithm == peakFinder3:
    print("Worst complexity should be theta(log(N))")
if algorithm == peakFinder22:
    print("Worst complexity should be theta(N^2)")
if algorithm == peakFinder23:
    print("Worst complexity should be N(log(N))")
