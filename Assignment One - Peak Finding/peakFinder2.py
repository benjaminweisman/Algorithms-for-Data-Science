import numpy as np
import numpy.random as nprnd
import matplotlib.pyplot as pplot

cnt = 0

def peakFinder2(ar):
    global cnt
    p=ar[0]
    j=1
    n=(len(ar))
    if (p < ar[j]) and (j < n + 1):
        cnt = cnt +1
        p=ar[j]
        j=j+1
    return p



def build_counting_arrays(array_of_n, array_of_timings,function_to_time):
    global cnt
    n_i=128
    for _ in range(50):
        arr = nprnd.randint(0,1000000,n_i)
        arr = np.sort(arr)
        array_of_n.append(n_i)
        
        # Timed function
        arr_copy = arr
        cnt = 0 # bad programming form here (global)
        function_to_time(arr_copy)
        array_of_timings.append(cnt)

        # Check if your function executed correctly (if you are writing your own function)
        #if not function_to_time.check_sort(arr_copy): print "quickSort_slow sort failed"
    
        # Increase the size of the array
        n_i = int(1.25*n_i)

array_of_n = []
array_of_timings = []
build_counting_arrays(array_of_n,array_of_timings,peakFinder2)
    
# Plots

pplot.plot(array_of_n,np.array(array_of_timings), label = 'Peak Finder 2')
pplot.legend()
pplot.show()
quit()

