import random

randArray = []
for i in range(0,20):
    rand = random.randint(1,50)
    randArray.append(rand)

def oneDimPeakFinder(arr):

    if len(arr) == 0:
        return None
    
    if len(arr) == 2:
        return arr[1]
    
    median = len(arr)//2

    if arr[median-1] < arr[median] and arr[median] > arr[median+1]:
        return arr[median]
    
    if arr[median-1] >= arr[median]:
        p = oneDimPeakFinder(arr[0:median])
        if p:
            return p

    if median >= 1 and arr[median+1] >= arr[median]:
        p = oneDimPeakFinder(arr[median:len(arr)])
        if p:
            return p
        
print(randArray)
print(oneDimPeakFinder(randArray))
