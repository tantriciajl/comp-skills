# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:09:38 2020

@author: Tricia Tan
"""

from pylab import *

# set constants
l = 10 # length of pendulum
m = 1 # mass of pendulum
t_max = 10 # max time
g = 9.81 # gravitational acceleration

# set no. of iterations
itn = 1000

# set time step 
dt = t_max/itn

# create arrays to store data
x = zeros(itn) # angular displacement
w = zeros(itn) # angular speed
t = zeros(itn) # time
E = zeros(itn) # energy

# set initial conditiions
x[0] = 5
t[0] = 0
w[0] = 0

# generate t, v and x data
for n in range(1,itn):
    t[n] = dt * n 
    w[n] = w[n-1] - (g * sin(x[n-1]) / l) * dt
    x[n] = x[n-1] +  dt * w[n] 

# generate E data
for n in range(0,itn):
    E[n] = m * g * l * cos(x[n]) + ( 0.5 * m * (w[n] * l)**2)