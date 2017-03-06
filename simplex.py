#input nxm matrix with n-1 vector
#Use bland's rule to resolve cycling
'''
understood from
The Design & Analysis of algorithms
by Anthony Levitin
'''

def simplex_method(matrix,relations):

    answer = [0]*len(matrix[0])
    
    #add slack variables
    for i,rel in enumerate(relations):
            
            col = [0]*(len(matrix))
            
            if rel == '<=':
                col[i] = 1
            if rel == '>=':
                col[i] = -1

            for x,c in enumerate(col):
                matrix[x].insert(len(matrix[x]) - 1,c)
    
    matrix_width = len(matrix[0])
    matrix_height = len(matrix)
    
    
    negative_entries = True

    while negative_entries:
        negative_entries = False
        for i in matrix[matrix_height - 1]:
            if i < 0:
                negative_entries = True
                break
    
    
        
        
        #find pivot column. will be first negative value in last row.     
        pivot_col = -1

        
        for i in xrange(matrix_width):
            #selects largest column for blands rule
            if matrix[matrix_height-1][i] < 0:
                pivot_col = i
                
                
        if pivot_col < 0:
            answer[len(answer) -1] = matrix[matrix_height- 1][matrix_width-1]
            return answer
        
        else:
            min_ratio = 0 
            pivot_row = 0
            no_positive = True
            first = True
            
            #move down the two columns, the pivot column and the value column
            for x,y,z in zip(matrix[:matrix_height- 1],matrix[:matrix_height-1],xrange(matrix_height-1)):
                
                if x[pivot_col] > 0:
                    no_positive = False
                    
                    #selects smallest row for blands rule
                    if y[matrix_width - 1]/x[pivot_col] < min_ratio or first:
                        min_ratio = y[matrix_width - 1]/x[pivot_col]
                        print y[matrix_width - 1]/x[pivot_col]
                        pivot_row = z
                        first = False
            
            if no_positive == True:
                return 'unbounded'

            print matrix[pivot_row]
            #divide each by entry in the row by the selected entry
            matrix[pivot_row] = [i/matrix[pivot_row][pivot_col] for i in matrix[pivot_row]]
            print matrix[pivot_row]
                

            #subtract the pivot row from each of the other rows
            for i in xrange(matrix_height):
                for x in xrange(matrix_width):
                    if i != pivot_row:
                        matrix[i][x] -= matrix[pivot_row][x]*matrix[i][pivot_col]
                        
                        print 'pivot c' + str(pivot_col) + str(i)
                        print matrix[i][pivot_col]
                        print matrix
            
            answer[pivot_col] = matrix[pivot_row][matrix_width - 1]
            
    answer[len(answer)-1] = matrix[matrix_height -1][matrix_width - 1]
    return answer

print simplex_method([[1.0,1.0,4.0], [1.0,3.0,6.0], [-3.0,-5.0,0.0]],['<=','<='])      
        

    
            
            
            
        
            
            
