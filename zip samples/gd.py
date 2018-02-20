import numpy as np
from numpy.polynomial.polynomial import polyval
import matplotlib.pyplot as plb


data = np.array([[20,80],[1,110],[2,90],[33,50],[34,40],[34,54],[34,43],[36,110],[200,1]],dtype=np.float64)

params=np.array([.7,.3])


rate = 0.00005
first = True
last_dif =0
dif = 1

def get_score(points,params):
    sums = np.zeros(len(params))
    
    for i in range(len(params)):
        for point in data:
            sums[i] +=  (polyval(point[0],params) -point[1])*(point[0]**i)
            
    return sums/len(points)
            


sums = rate * get_score(data,params)
last_sums = sums

#do assignments
params = params - sums
sums = rate * get_score(data,params)
dif = np.abs(np.sum((sums - last_sums)))

while last_dif > dif or first:
    first = False
    last_dif = dif
    last_sums = sums
    
    #do assignments
    params = params - sums
    sums = rate * get_score(data,params)
    dif = np.abs(np.sum((sums - last_sums)))    
    
    
X = np.linspace(-10,200,100)
Y= np.array([polyval(x,params) for x in X])


plb.plot(X,Y)
plb.plot([d[0] for d in data],[d[1] for d in data],'ro')
plb.show()
    
    
    
    
    
