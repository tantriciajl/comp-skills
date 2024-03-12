# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:25:43 2020

@author: tricia
"""
from pylab import *

import numpy

# setting constants
t_max = 10
dt = 0.01
g = -9.81
m = 4
k = 0.07

# creating array to store data
t = zeros( int(t_max/dt) )
h = zeros( int(t_max/dt) )
v = zeros( int(t_max/dt) )

# setting initial values
h[0] = 50
t[0] = 0
v[0] = 0

# generating data
for n in range(1,int( t_max/dt )):
    t[n] = t[n-1] + dt
    v[n] = v[n-1] + (g + (k*(v[n-1]**2))/m) * dt
    h[n] = h[n-1] + ( dt * v[n] )
    if h[n] < 0:
        break

# plotting graphs of data
subplot(2,1,2)
plot(t[h>0],h[h>0], 'r')
xlabel("Time (s)")
ylabel("Position (m)")
grid()

subplot(2,1,1)
plot(t[h>0],v[h>0], 'y')
xlabel("Time (s)")
ylabel("Velocity (ms^-1)")
title("Cat Falling From a Window")
grid()

# fitting 2nd order polynomial to h vs t
h_coeff = polyfit(t[h>0],h[h>0], 2)
ph = poly1d( h_coeff )

# finding time at h = 0
gh = roots(ph)

print("\n3)b) The cat hits the ground at t = %.3f s.\n\n Its velocity is %.3f ms^-1." % (gh[1],min(v)) )

print("\n3)d) The cat hasn't reached terminal velocity yet because the velocity-time graph doesn't show a linear curve at any point, meaning the cat continues to accelerate until it hits the ground.") 

