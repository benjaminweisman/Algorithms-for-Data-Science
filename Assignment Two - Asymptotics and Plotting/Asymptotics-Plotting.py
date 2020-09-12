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



def problem3a(arr):
    ar=[]
    for x in arr:
        x=x**2
        ar.append(x)
    return ar

def problem3b(arr):
    ar=[]
    for x in arr:
        x=np.sqrt(x)
        ar.append(x)
    return ar

def problem3c(arr):
    ar=[]
    for x in arr:
        x=2**x
        ar.append(x)
    return ar

def problem3d(arr):
    ar=[]
    for x in arr:
        x=np.log2(x)
        ar.append(x)
    return ar

def problem3e(arr):
    ar=[]
    for x in arr:
        x=.5**x
        ar.append(x)
    return ar

def problem3f(arr):
    ar=[]
    for x in arr:
        x=x*np.log2(x)
        ar.append(x)
    return ar

def problem3g(arr):
    ar=[]
    for x in arr:
        x=x
        ar.append(x)
    return ar

def problem3h(arr):
    ar=[]
    for x in arr:
        x=x**3
        ar.append(x)
    return ar

print(A)
print(problem3h(A))
    


#list of N's
seq = [x for x in range(20, 801) if x % 20 == 0]
times=[]
times2=[]

new1=[]
new2=[]
timings = []
timings2=[]

#TYPE ALGORITHM HERE
algorithm = problem2a
#IF USING PAIR, TRUE
pair = True
if pair==True:
    #TYPE ALGORITHM 2 HERE
    algorithm2 = problem2b
#DIMENSIONS OF ARRAY
dimensions = 1



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
    R=100
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
    print("Intersecting on: ")
    print(np.intersect1d(new1,new2))
else:
    pplot.plot(seq, np.array(times), label = str(algorithm))


'''
deltas = np.diff(times)
print("Deltas between each N")
print(deltas)
'''

pplot.legend()
pplot.show()
quit()





