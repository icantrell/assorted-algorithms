import math
import operator
import xgcd
#will need our old sieve de eratoshenes algorithm, which we will use to find our squares
from sieve_de_eratosthenes import sieve_de_eratosthenes
from quadratic_gaussian_elimination import quadratic_gaussian_elimination
from quadratic_gaussian_elimination import transpose

#1000
#255

n = input('enter number to factored:')
b = input('enter the smooth number bound:')



def get_congruent_squares(n,b):
        primes = sieve_de_eratosthenes(b)
        start = int(math.sqrt(n)) + 2

        xs = []
        ys = []
        y_vecs = []
        i = 0
        while True:
                if len(xs) == len(primes) + 1:
                        break
                
                x = start + i
                y = ((x)**2)%n
                
           
                y_temp = y
                y_vec = [0] * len(primes)
                for index,p in enumerate(primes):
                        while y_temp % p == 0 and y_temp != 0 and y_temp != 1: 
                                y_temp /= p
                                y_vec[index] += 1
                                y_vec[index] %= 2
                
                        
                '''
                if y_vec == [0] * len(primes) and (y_temp == 1 or y_temp == 0):
                       return (x,y)
                       
                               
                inverse = xgcd.xgcd(n,y_temp)
                if inverse[0] == 1:
                        
                        x = x * inverse[2] %n
                        
                        y = y * inverse[2] %n
                        
                        y_temp = 1
                '''
                if y_temp == 0:
                        print 'IM here'
                if y_temp == 1 or y_temp == 0:
                        ys.append(y)
                        xs.append(x)
                        y_vecs.append(y_vec)
                              
                
                i+=1

        
        print ys       
        print primes
        answer_vec = quadratic_gaussian_elimination(transpose(y_vecs))
        print answer_vec
        
        vector = [j*k if j*k != 0 else 1 for j,k in zip(ys,answer_vec)]
        print vector

        answer = reduce(operator.mul,vector,1)
        print answer
        big_y = int(math.sqrt(answer))
        print big_y

        print xs
        vector = [j*k if j*k != 0 else 1 for j,k in zip(xs,answer_vec)]

        big_x = reduce(operator.mul,vector,1)
        print big_x**2
        print big_x - big_y
        print (big_x + big_y) % n
        return xgcd.xgcd(n, big_x - big_y)
        
        

print get_congruent_squares(n,b)



                
        
        
        
        
