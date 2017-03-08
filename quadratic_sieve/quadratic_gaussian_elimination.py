import copy

def transpose(old_mat,n=1):

    mat = old_mat

    for t in xrange(n):
        new_mat =[[]]*len(mat[0])
        for i in xrange(len(mat[0])):
            new_mat[i]=[0]*len(mat)
            
        
        for i in xrange(len(mat)):
            x1 = 0
            for x in xrange(len(mat[i]) - 1,-1,-1):
                new_mat[x1][i] = mat[i][x]
                x1 += 1

        mat = new_mat
            
    return new_mat


def quadratic_gaussian_elimination(mat0):
    mat = copy.deepcopy(mat0)
    h = len(mat)
    w = len(mat[0])
    column = 0
    pivots = []
    
    #make reduced row echelon form
    #find max row and swap
    for i in xrange(h):
        
        

        #terminate if all pivots are set
        if i+column >= w:
            break
        
        #adjust for pivot column
        while i+column < w:
            column_selected = False
            for y in xrange(i,h):
                if mat[y][i + column] != 0:
                    #is a pivot column
                    column_selected = True
                    pivots.append((i,i+column))
                    break
                
            if not column_selected:
                #if column is not a pivot column move to next column and skip iteration
                column +=1
            else:
                break
            
        if i + column < w:
            #only run this section when there is a pivot
            #get pivot row
            maxrow = i
            for x in xrange(i + 1, h):
                if abs(mat[x][i + column]) > abs(mat[maxrow][i + column]):
                    maxrow = x
            (mat[i], mat[maxrow]) = (mat[maxrow], mat[i])
            
            #make all lower entries in column zeros
            for x in xrange(i + 1, h):
                c = mat[x][i + column]/ mat[i][i + column]
                for y in xrange(i+column,w):
                    mat[x][y] -= mat[i][y] * c
                    mat[x][y] %= 2

        
    print mat           
    #we will set all variables to 1, x1=x2=...x3 =1
    a = [1 for i in xrange(w)]
    #reverse for back substitution
    pivots.reverse()
    for i in pivots:
        #if xi is a pivot xi = xk + xt + xu +... -1 (subtract 1 for pivot itself)
        a[i[1]] = ((sum([j*k for j,k in zip(mat[i[0]],a )] )) - 1 )%2
            
    return a
'''
mat = [[0,0,0,1,0,1],
       [0,1,1,0,1,0],
       [1,1,0,0,0,1],
       [0,0,1,0,0,0],
       [0,0,1,0,1,0]]
print quadratic_gaussian_elimination(mat)


#transposed
mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 1, 0, 0, 0, 1]]

#untransposed for reference
mat2 = [[0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0]]


vector=  quadratic_gaussian_elimination(mat)
print vector

this = []
for i in mat:

    this.append(sum(j * k for j,k in zip(vector,i))%2)

#must be the zero vector
print this
'''
