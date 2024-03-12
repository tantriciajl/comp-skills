# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:31:37 2020

@author: Tricia Tan


"""

from pylab import *

# set constants
k = 10
m = 1
t_max = 10

# set no. of iterations
itn = 1000

# set time step 
dt = t_max/itn

# create arrays to store data
x = zeros(itn)
v = zeros(itn)
t = zeros(itn)
E = zeros(itn)

# set initial conditiions
x[0] = 5
t[0] = 0
v[0] = 0

# generate t, v and x data
for n in range(1,itn):
    t[n] = dt * n
    v[n] = v[n-1] -  (k * x[n-1] / m) * dt 
    x[n] = x[n-1] +  dt * v[n] 

# generate E data
for n in range(0,itn):
    E[n] = m * g * l * cos(x[n]) + ( 0.5 * m * (w[n] * l)**2