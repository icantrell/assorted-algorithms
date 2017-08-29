#Levinstein
import matplotlib.pyplot as plt
import numpy as np
import time

def Levinstein(s0, s1):
    if s0 == '':
        return len(s1)
    
    if s1 == '':
        return len(s0)
    
    cost = 0
    
    if s0[-1] != s1[-1]:
        cost = 1
        
    return min(Levinstein(s0,s1[:-1]) + 1,\
               Levinstein(s0[:-1],s1) + 1,\
               Levinstein(s0[:-1],s1[:-1]) + cost)



print(Levinstein('asdf','basfg'))
print(Levinstein('asdwerf','asfadgrg'))
print(Levinstein('asdagf','astryfg'))
print(Levinstein('asadgdf','asfdfghg'))





   
