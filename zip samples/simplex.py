#input nxm matrix with n-1 vector
#Use bland's rule to resolve cycling



def simplex_method(matrix,relations):

    answer = [0.0]*len(matrix[0])
    
    #add slack variables
    for i,rel in enumerate(relations):
            
            col = [0]*(len(matrix))
            
            if rel == '<=':
                col[i] = 1.0
            if rel == '>=':
                col[i] = -1.0

            for x,c in enumerate(col):
                matrix[x].insert(len(matrix[x]) - 1,c)
    
    matrix_width = len(matrix[0])
    matrix_height = len(matrix)
    
    
    while 1:    
        #find pivot column. will be first negative value in last row.     
        pivot_col = -1

        
        for i in range(matrix_width):
            #selects largest column for blands rule
            if matrix[matrix_height-1][i] < 0:
                pivot_col = i
                break
                
                
        if pivot_col < 0:
            #get the answers from the matrix
            #for each column
            for x in range(len(answer) - 1):
                answer_column = True
                num_ones = 0
                row_number = 0
                #for each row
                for i ,row in enumerate(matrix[:matrix_height-1]):
                    if row[x] == 1:
                        num_ones += 1
                        row_number = i
                    elif row[x] != 0:
                        answer_column = False
                if num_ones == 1 and answer_column:
                    answer[x] = matrix[row_number][matrix_width - 1]
            
            #set value of z
            answer[len(answer) - 1] = matrix[matrix_height-1][matrix_width-1]
            return answer
        
        else:
            min_ratio = 0 
            pivot_row = 0
            negative_column = True
            #functions like a do while loop
            first = True
            
            #move down the two columns, the pivot column and the value column
            for x,y,z in zip(matrix[:matrix_height- 1],matrix[:matrix_height-1],range(matrix_height-1)):
                
                if x[pivot_col] > 0:
                    negative_column = False
                    
                    #selects smallest row for blands rule
                    if y[matrix_width - 1]/x[pivot_col] < min_ratio or first:
                        min_ratio = y[matrix_width - 1]/x[pivot_col]
                        pivot_row = z
                        first = False
            
            if negative_column == True:
                return 'unbounded'

           
            #divide each by entry in the row by the selected entry
            matrix[pivot_row] = [i/matrix[pivot_row][pivot_col] for i in matrix[pivot_row]]
            
                

            #subtract the pivot row from each of the other rows
            for i in range(matrix_height):
                multiplier = matrix[i][pivot_col]
                for x in range(matrix_width):
                    if i != pivot_row:
                        matrix[i][x] -= matrix[pivot_row][x]*multiplier
                        
           
                
    
#problem from pdf
answer= simplex_method([[3.0,2.0,66.0],
                        [2.0,4.0,180.0],
                      [2.0,10.0,200.0],
                      [-90.0,-75.0,0.0]],['<=','<=','<=']) 
print( "chairs: " + str(answer[0]))
print ("sofas: " + str(answer[1]))
print("profit: " + str(answer[2]))
            
            
