# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:32:24 2020

@author: tricia
"""
from pylab import *

# 1s time step
g = -9.81
t_max = 10
dt = 1

y = zeros(int(t_max/dt))
v = zeros(int(t_max/dt))
t = zeros(int(t_max/dt))

y[0] = 0
v[0] = 46
t[0] = 0

for n in range(1,t_max):
    t[n] = t[n-1] + dt
    v[n] = v[n-1] + g * dt
    y[n] = (v[n-1] * dt) + (0.5 * g * (dt**2)) + y[n-1]
    
subplot(2,1,2)
plot(t, y,'b') # figure 1
xlabel("Time (s)")
ylabel("Vertical Displacement (m)")
title("Trajectory of a Ball (Time Step 1s)")
grid()

subplot(2,1,1)
plot(t,v,'b') # figure 1
xlabel("Time (s)")
ylabel("Velocity  (m)")
title("Velocity of a Ball (Time Step 1s)")
grid()

# finding max height of ball
print("\n2)a) The maximum height of the ball is %.3f m.\n" % max(y))

# 0.1s time step
dt1 = 0.1

y1 = zeros(int(t_max/dt1))
v1 = zeros(int(t_max/dt1))
t1 = zeros(int(t_max/dt1))

y1[0] = 0
v1[0] = 46
t1[0] = 0

for n in range(1,int(t_max/dt1)):
    t1[n] = t1[n-1] + dt1
    v1[n] = v1[n-1] + g * dt1
    y1[n] = (v1[n-1] * dt1) + (0.5 * g * (dt1**2)) + y1[n-1]

figure() 
subplot(2,1,2)
plot(t1,y1,'g') # figure 2
xlabel("Time (s)")
ylabel("Vertical Displacement (m)")
title("Trajectory of a Ball (Time Step 0.1s)")
grid()

subplot(2,1,1)
plot(t1,v1,'g') # figure 2
xlabel("Time (s)")
ylabel("Velocity  (m)")
title("Velocity of a Ball (Time Step 0.1s)")
grid()

print("2)d) The maximum height of the ball is %.3f m.\n" % max(y1) )

# 0.01s time step
dt2 = 0.01

y2 = zeros(int(t_max/dt2))
v2 = zeros(int(t_max/dt2))
t2 = zeros(int(t_max/dt2))

y2[0] = 0
v2[0] = 46
t2[0] = 0

for n in range(1,int(t_max/dt2)):
    t2[n] = t2[n-1] + dt2
    v2[n] = v2[n-1] + g * dt2
    y2[n] = (v2[n-1] * dt2) + (0.5 * g * (dt2**2)) + y2[n-1]

figure() 
subplot(2,1,2)
plot(t2,y2,'r') # figure 2
xlabel("Time (s)")
ylabel("Vertical Displacement (m)")
title("Trajectory of a Ball (Time Step 0.01s)")
grid()

subplot(2,1,1)
plot(t2,v2,'r')
xlabel("Time (s)")
ylabel("Velocity (m)")
title("Velocity of a Ball (Time Step 0.01s)")
grid()

print("The maximum height of the ball is %.3f m.\n" % max(y2) )

# finding exact answer
p = poly1d([-4.905, 46, 0])
p_diff = polyder(p)
roots(p_diff)

print("The exact answer is %.3f m which figure 3 generates the closest value to." % p( roots(p_diff) ) )
