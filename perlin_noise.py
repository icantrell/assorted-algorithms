def interpolate(x0,x1,w):
    return (1 - w)*x0 + w*x1

def get_gradient(coord):
    #use srand for each dimension
    #so that (rand(n),rand(n),...) never occurs.

def dot(v1,v2):
    result = 0
    for i,x in zip(v1,v2):
        result += i*x
    return result
    
def perlin(coord):
    corners = []
    vec = []
    
    for i in xrange(2**len(coord)):
        corners.append([])

        for x in xrange(len(coord)):
            if coord[x]<0:
                corners[i].append(float(int(coord[x]) - 1))
            else:
                corners[i].append(float(int(coord[x])))
                
            corners[i][x] += i&2**x
            vec[x] = coord[x] - corners[i][x]
            
        dot(get_gradient(corners[i],vec)

        
