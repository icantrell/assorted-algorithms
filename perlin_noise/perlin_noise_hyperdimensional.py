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
        #set seeds for procedural gradients at vertecies.
        random.seed((i+1)*int(coord[i]))
        gradient.append(random.random())
        #use srand for each dimension
        #so that (rand(n),rand(n),...) never occurs.
        
    #normalize the vector
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
            #floor the coordinate components.
            if coord[x]<0:
                corners[i].append(float(int(coord[x]) - 1))
            else:
                corners[i].append(float(int(coord[x])))
            #add 1 to each vector's components depending on their index.
            #i will range through from (0) to (2**(n) - 1) so changing i's binary forms
            #into a vectors will cover each point on the hypercube of n dimensions.
            #And we can use 2**x for {x:0 to (n-1)} to add to the individual components.
            if i&2**x:
                corners[i][x] += 1
            #get vector of corner to coordinate.
            vec.append(coord[x] - corners[i][x])
        
        #get dot prod of vector and it's corresponding gradient.    
        dot_products.append(dot(get_gradient(corners[i]),vec))
    
    #vector used for interpolation
    interpolate_vec = [coord[i] - corners[0][i] for i in xrange(len(coord))]
    
    interpolated_values = dot_products  
    #interpolate along each dimension.
    for dim in xrange(len(coord),0,-1):
        #in each dimensions here will be 2**(dim-1) interpolations.
        for i in xrange(2**(dim-1)):
            #interpolate along axes from largest to smallest. e.g y axis(1) then x axis(0)
            interpolated_values[i] = interpolate(interpolated_values[i], interpolated_values[i + 2**(dim-1)], interpolate_vec[dim-1])
            
    return interpolated_values[0]

xs =[]
ys =[]
    
for i in xrange(100):
    xs.append(i/50.0)
    ys.append(perlin((i/50.0)))

plt.plot(xs,ys)
plt.show()