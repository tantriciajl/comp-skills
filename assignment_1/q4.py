# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:13:29 2020

@author: Tricia Tan :)
"""

# creating equation for x(t)
t = linspace( 0, 20, 100 )
p_x = poly1d([0, 120*cos( deg2rad(40) ), 0])
x = p_x(t)

# creating equation for y(t)
p_y = poly1d([-4.9, 120*sin( deg2rad(40) ), 90])
y = p_y(t)

# plotting x(t) 
plot( t, x, label = "x(t)" )

# plotting y(t)
plot( t, y, label = "y(t)" )

# finding max height
dy = polyder(p_y)
print("\nb)i) The maximum height is %.3f m and occurs at t = %.3f s.\n" % ( p_y( roots(dy) ), roots(dy) ) )

# finding time projectile hits the ground
t_ground = roots(p_y)
print(t_ground)

# finding horizontal distance when projectile hits the ground
print("\nb)ii) The projectile hits the ground at %.3f s and it has travelled a horizontal distance of %.3f m." % ( t_ground[0], p_x( t_ground[0] ) )  )

# making array between 0-15 seconds
t_c = arange(0, 15.1, 0.1)
x_c = p_x(t_c)
y_c = p_y(t_c)

# finding the max height in this array
print( "\nc)i) The maximum value in the height array is %.3f and occurs at a time of %.3f." % (max(y_c), t_c[argmax(y_c)]) )
print( "\nThe maximum height is lower and the time at which this occurs is greater than in part b)i).\n" )

# finding times at which height is greater than 150 m
f = t_c[y_c>150]
print(len(f))
print( "\nc)ii) The range of times for which the height is greater than 150 m is between %.3f and %.3f s.\n" % (f[0], f[140]) )
g = x_c[y_c>150]
print(len(g))
print( "\nThe range of horizontal positions for which this occurs is between %.3f and %.3f m." % (g[0], g[140]) )

# formatting graph
legend(loc='best')
xlabel( "Time (s)" )
ylabel( "Distance (m)" )
title( "Projectile Motion" )
grid()