def legendre_symbol(a, p):
    """
    Legendre symbol
    Define if a is a quadratic residue modulo odd prime
    http://en.wikipedia.org/wiki/Legendre_symbol
    """
    ls = pow(a, (p - 1)/2, p)
    if ls == p - 1:
        return -1
    return ls
'''
https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm
'''
def shanks_tonelli(n,p):
    S = 0
    q = p - 1
    while q%2 == 0:
        q/=2
        S += 1
        
    #if R**2 == n*t algorithm terminates 
    R = pow(n,(q+1)/2,p)
    t = pow(n,q,p)
    M = S
    
    z = 0
    for i in xrange(p):
        if legendre_symbol(i,p) == -1:
            z = i
            break
    c = pow(z,q,p)    
    
    while t != 1 and t != 0:
        i = 0
        g = 0
        while g!=1:
            g= pow(t,2**i,p)
            i+=1

        
        
        y = M - i - 1
        if y < 0:
            return None
        
        b = pow(c,2**(y),p)

        R = (R*b)%p

        t = (t*(b**2))%p
        c = pow(b,2,p)
        M = i
    return R


print shanks_tonelli(0,19)
print shanks_tonelli(1,19)
print shanks_tonelli(2,19)
print shanks_tonelli(3,19)
print shanks_tonelli(4,19)
print shanks_tonelli(5,19)
print shanks_tonelli(6,19)
print shanks_tonelli(7,19)
print shanks_tonelli(8,19)
print shanks_tonelli(9,19)
print shanks_tonelli(10,19)
print shanks_tonelli(11,19)
print shanks_tonelli(12,19)
print shanks_tonelli(13,19)
print shanks_tonelli(14,19)
print shanks_tonelli(15,19)
print shanks_tonelli(16,19)
print shanks_tonelli(17,19)
print shanks_tonelli(18,19)




       
    
  
#self organizing map
#bots

