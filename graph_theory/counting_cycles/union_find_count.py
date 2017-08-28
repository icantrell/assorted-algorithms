import numpy as np

A = np.array([[0,1],
              [0,2],
              [1,4],
              [3,4],
              [1,3],
              [3,3]])




#input number of nodes to construct B and list of edges
B = np.array([0,1,2,3,4])


def get_parent(n):
    '''
    Finds the ultimate parent of the nth vertex. By using the table B.
    The parent will refer to itself as it's predecessor.
    '''
    o = n
    j = B[n]
    while n != j:
        n =B[j]
        j=B[n]
    B[o] = j
    return j

number_of_joins = 1        
loops = 0 

#for each edge.
for i in range(len(A)):
    e = A[i]

    if number_of_joins == len(B):
        loops += len(A) - i
        break    
    
    #get ultimate parent of each vertex attached to the edge.
    pi = get_parent(e[0])
    px = get_parent(e[1])
    
    #if have same parent then connecting them will form a cycle.
    if pi == px:
        loops += 1
    else:
        number_of_joins += 1
        #if different parents then make px's parent the same as pi's.
        B[px] = pi
        
    
                
print('number of loops: {}'.format(loops))
                    
