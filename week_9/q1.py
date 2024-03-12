# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:39:52 2020

@author: tricia
"""
from pylab import *

# inputting number to take factorial of
num = int( input("1)a) Please enter a positive integer to find the factorial of\n") )

f = zeros(num+1)
f[0] = 1

# check if number is -, + or 0
for n in range(1,num + 1): # num stays the same as the initial value - despite it being redefined in the loop
    f[n] = f[n-1] * num # so this code only loops everything below the "for n in range(1,num + 1):"
    num = num - 1

print("The answer is %d" % f[n] )

M = int( input("\n1)b) Please enter another integer \n") )

f = zeros(M)
f[0] = 1

for n in range(1,M): 
    f[n] = f[n-1] * (n + 1)
    if f[n] > M:
        print("\n1)b) %d! is greater than %d" % (n+1, M) ) # n + 1 because it counts positions starting from 0
        break