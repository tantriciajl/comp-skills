# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:50:34 2020

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
    x[n] = x[n-1] +  dt * v[n-1] 

# generate E data
for n in range(0,itn):
    E[n] = 0.5 * k * (x[n]**2) + 0.5 * m * (v[n]**2)
    
# plot data
subplot(2,1,1)
plot(t, x, 'r', label='Euler Method')
xlabel("Time (s)", fontsize=12)
ylabel("Displacement (m)", fontsize=12)
title("Displacement of a Simple Harmonic Oscillator", fontsize=16)
legend(loc='best')
grid()

subplot(2,1,2)
plot(t, v, 'y', label='Euler Method')
xlabel("Time (s)", fontsize=12)
ylabel("Velocity (ms^-1)", fontsize=12)
title("Velocity of a Simple Harmonic Oscillator", fontsize=16)
legend(loc='best')
grid()

figure()
plot(t, E, 'm', label="Euler Method")
xlabel("Time (s)", fontsize=12)
ylabel("Energy (J)", fontsize=12)
title("Energy of a Simple Harmonic Oscillator", fontsize=16)
legend(loc='best')
grid()

# calculate final energy
z = max(E)/min(E)

print("\n1)d) The energy has increased by %.3f times the initial energy at the end of the simulation.\n" % z)


    