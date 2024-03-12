# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:26:57 2020

@author: Tricia Tan

CRITICAL DAMPING
"""

from pylab import *

# set constants
k = 10
m = 1
c = 2 * (k * m)**0.5
t_max = 10

# set no. of iterations
itn = 1000

# set time step 
dt = t_max/itn

# create arrays to store data
x = zeros(itn)
v = zeros(itn)
t = zeros(itn)

# set initial conditiions
x[0] = 5
t[0] = 0
v[0] = 0

# generate t, v and x data
for n in range(1,itn):
    t[n] = dt * n
    v[n] = v[n-1] -  ( (k * x[n-1] / m) + (c * v[n-1] / m)  ) * dt 
    x[n] = x[n-1] +  dt * v[n] 
   
# plot graph for c
subplot(2,1,1)
plot(t,x,'r')
xlabel("Time (s)", fontsize = 12)
ylabel("Displacement (m)", fontsize = 12)
title("Critical Damping", fontsize = 16)
grid()

subplot(2,1,2)
plot(t,v,'y')
xlabel("Time (s)", fontsize = 12)
ylabel("Velocity (ms^-1)", fontsize = 12)
grid()

# find critical damping constant c
print("\n3)b) The value of c for critical damping is %.3f.\n" % c)

    
    
"""QUARTER CRITICAL DAMPING"""

#set constant
c1 = (2 * (k * m)**0.5)/4

# set time step 
dt = t_max/itn

# create arrays to store data
x1 = zeros(itn)
v1 = zeros(itn)
t1 = zeros(itn)

# set initial conditiions
x1[0] = 5
t1[0] = 0
v1[0] = 0

# generate t, v and x data
for n1 in range(1,itn):
    t1[n1] = dt * n1
    v1[n1] = v1[n1-1] -  ( (k * x1[n1-1] / m) + (c1 * v1[n1-1] / m)  ) * dt 
    x1[n1] = x1[n1-1] +  dt * v1[n1] 
   
# plot graph for c
figure()
subplot(2,1,1)
plot(t1,x1,'r')
xlabel("Time (s)", fontsize = 12)
ylabel("Displacement (m)", fontsize = 12)
title("1/4 Critical Damping", fontsize = 16)
grid()

subplot(2,1,2)
plot(t1,v1,'y')
xlabel("Time (s)", fontsize = 12)
ylabel("Velocity (ms^-1)", fontsize = 12)
grid()



"""FOUR TIMES CRITICAL DAMPING"""

# set constants
c2 = (2 * (k * m)**0.5)*4

# set no. of iterations
itn = 1000

# set time step 
dt = t_max/itn

# create arrays to store data
x2 = zeros(itn)
v2 = zeros(itn)
t2 = zeros(itn)

# set initial conditiions
x2[0] = 5
t2[0] = 0
v2[0] = 0

# generate t, v and x data
for n2 in range(1,itn):
    t2[n2] = dt * n2
    v2[n2] = v2[n2-1] -  ( (k * x2[n2-1] / m) + (c2 * v2[n2-1] / m)  ) * dt 
    x2[n2] = x2[n2-1] +  dt * v2[n2] 
   
# plot graph for c
figure()
subplot(2,1,1)
plot(t2,x2,'r')
xlabel("Time (s)", fontsize = 12)
ylabel("Displacement (m)", fontsize = 12)
title("x4 Critical Damping", fontsize = 16)
grid()

subplot(2,1,2)
plot(t2,v2,'y')
xlabel("Time (s)", fontsize = 12)
ylabel("Velocity (ms^-1)", fontsize = 12)
grid()
