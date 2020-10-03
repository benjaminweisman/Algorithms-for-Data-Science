import random
import matplotlib.pyplot as pplot
import time


random.seed(100)
m=[None]*1021
rands1000 = []
rands50=[]
#sufficiently large prime number
p=3011
times=[]
timings=[]


for i in range (0,1000):
    rands1000.append(random.randrange(1000000000,9999999999,1))


for j in range(0,50):
    rands50.append(random.randrange(1,1000))
    
#ensuring only unique values
random.shuffle(rands50)

#rands50.append(random.sample(range(1000),50))

for x in rands1000:
    #xmodp
    z=x%p
    #zmod1021
    q=z%1021
    while m[q] != None:
        q+=1
    m.pop(q)
    m.insert(q,x)

#print(m)
#print(len(m))
def search():
    for h in rands50:
        start = time.time()
        #searching for each key in our hash table
        print (m[h])
        end = time.time()
        timings.append(end-start)


search()
print(timings)
pplot.xlabel('Runtimes')
pplot.ylabel('Frequency')
pplot.hist(timings)
pplot.show()
pplot.close()
