import random
import math
import matplotlib.pyplot as plt

#interpolate between x0 and x1
def interpolate(x0,x1,w):
    return (1 - w)*x0 + w*x1

#get a normalized random gradient
def get_gradient(coord):
    gradient = []
    for i in xrange(len(coord)):
        random.seed((i+1)*int(coord[i]))
        gradient.append(random.random())
        #use srand for each dimension
        #so that (rand(n),rand(n),...) never occurs.
    #normalize vector
    magnitude = 0
    for i in xrange(len(gradient)):
        magnitude += gradient[i]*gradient[i]
    magnitude = math.sqrt(magnitude)
    
    for i in xrange(len(gradient)):
        gradient[i] = gradient[i]/magnitude
        
    return gradient

#take dot product of v1 and v2
def dot(v1,v2):
    result = 0
    for i,x in zip(v1,v2):
        result += i*x
    return result
    
def perlin(coord):
    #store corners vertices of the hypercube
    corners = []
    #store the dot products
    dot_products = []
    
    for i in xrange(2**len(coord)):
        corners.append([])
        vec = []
        
        for x in xrange(len(coord)):
            if coord[x]<0:
                corners[i].append(float(int(coord[x]) - 1))
            else:
                corners[i].append(float(int(coord[x])))
            #add 1 to each
            if i&2**x:
                corners[i][x] += 1
            vec.append(coord[x] - corners[i][x])
            
        dot_products.append(dot(get_gradient(corners[i]),vec))
    
    
    interpolate_vec = [coord[i] - corners[0][i] for i in xrange(len(coord))]
    
    interpolated_values = dot_products  
    for dim in xrange(len(coord),0,-1):
        #interpolate along each dimension.
        for i in xrange(2**(dim-1)):
            interpolated_values[i] = interpolate(interpolated_values[i], interpolated_values[i + 2**(dim-1)], interpolate_vec[dim-1])
            
    return interpolated_values[0]

xs =[]
ys =[]
    
for i in xrange(100):
    xs.append(i/50.0)
    ys.append(perlin((i/50.0)))

plt.plot(xs,ys)
plt.show()