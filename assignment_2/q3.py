# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:18:27 2020

@author: Tricia Tan
"""

from pylab import *

# 3)b) TIME STEP = 0.01s 

# setting constants
t_max = 5 # max time 
Ts = 0 # surrouding temperature
dt = 0.01 # time steps
k = 2 # rate of decrease

# creating arrays to store data
T = zeros( int(t_max/dt) + 1) # object's temperature
t = zeros( int(t_max/dt) + 1) # time

# setting initial values
T[0] = 1 
t[0] = 0 

# generating data
for n in range(1,int( t_max/dt ) + 1):
    t[n] = t[n-1] + dt
    T[n] = T[n-1] - (dt * k) * (T[n-1] - Ts)

# plot data generated
plot(t, T, label="time step = 0.01s")
title("Newton's Law of Cooling (k = -2)")
xlabel("Time (s)")
ylabel("Temperature (degrees celsius)")
legend(loc='best')

savefig("newtons_law_cooling_0.01.png")




# TIME STEP = 0.25s 

# re-setting constants
dt25 = 0.25 # time steps

# re-creating arrays to store data
T25 = zeros( int(t_max/dt25) + 1 ) # object's temperature
t25 = zeros( int(t_max/dt25) + 1) # time

# re-setting initial values
T25[0] = 1 
t25[0] = 0 

# generating data
for n in range(1,int( t_max/dt25 ) + 1):
    t25[n] = t25[n-1] + dt25
    T25[n] = T25[n-1] - (dt25 * k) * (T25[n-1] - Ts)

# plot data generated
figure()
plot(t25, T25, 'r', label="time step = 0.25s")
xlabel("Time (s)")
ylabel("Temperature (degrees celsius)")
title("Newton's Law of Cooling (k = -2)")
legend(loc='best')

savefig("newtons_law_cooling_0.25.png")




# 3)b) TIME STEP = 2s 

# re-setting constants
dt2 = 2 # time steps

# re-creating arrays to store data
T2 = zeros( int(t_max/dt2) + 1 ) # object's temperature
t2 = zeros( int(t_max/dt2) + 1 ) # time

# re-setting initial values
T2[0] = 1 
t2[0] = 0 

# generating data
for n in range(1,int( t_max/dt2 ) + 1):
    t2[n] = t2[n-1] + dt2
    T2[n] = Ts + (T2[n-1] - Ts) * e **(-k * t2[n])

# plot data generated
figure()
plot(t2, T2, 'g', label="time step = 2s")
xlabel("Time (s)")
ylabel("Temperature (degrees celsius)")
title("Newton's Law of Cooling (k = -2)")
legend(loc='best')

savefig("newtons_law_cooling_2.png")




# 3)c) HOT TEA

# re-setting constants
k = 0.002
dt_tea = 0.01 # time steps
Ts = 20 # surround temperature
t_max = 300 # 5 mins max time

# re-creating arrays to store data
T_tea = zeros( int(t_max/dt_tea) + 1 ) # object's temperature
t_tea = zeros( int(t_max/dt_tea) + 1 ) # time

# re-setting initial values
T_tea[0] = 90 
t_tea[0] = 0 

# generating data
for n in range(1,int( t_max/dt_tea ) + 1):
    t_tea[n] = t_tea[n-1] + dt_tea
    T_tea[n] = T_tea[n-1] - (dt_tea * k) * (T_tea[n-1] - Ts)

# create array for temperature <= 60C
tea = t_tea[T_tea<=60]

# create output file to save answers
c = open("newtons_cooling_answers.txt", 'w')

c.write("3)c) Tea is drinkable at around %.3f s.\n" % tea[0])

c.close()