import numpy as np

def fft(x):
    x = np.asarray(x)
    
    n = x.shape[0]
    
    if n == 1:
        return x[0]
    
    if n %2 != 0:
        pass #add zeros here
    
    even = fft(x[::2])
    odd = fft(x[1::2])
    
    factor = np.e**(np.complex(0,-2)*np.pi*np.arange(n)/n)
    
    return np.concatenate([even + factor[:n/2]*odd,even + factor[n/2:]*odd])


def ifft(x, norm= True):
    x = np.asarray(x)
    
    n = x.shape[0]
    if n %2 != 0:
        pass #add zeros here
    
    if n == 1:
        return x[0]
    
    even = ifft(x[::2], False)
    odd = ifft(x[1::2], False)
    
    factor = np.e**(np.complex(0,2)*np.pi*np.arange(n)/n)
    if norm:
        return np.concatenate([even + factor[:n/2]*odd,even + factor[n/2:]*odd])/n
    return np.concatenate([even + factor[:n/2]*odd,even + factor[n/2:]*odd])

r = np.random.randint(32)
q = np.random.randint(32)




x=fft(r)


                      
    