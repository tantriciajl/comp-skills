# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:56:32 2020

@author: Tricia Tan :)
"""

# inputting x and y values
x = arange(0.1, 1.1, 0.1)
y = array([1.1, 2.2, 3.1, 4.0, 4.8, 5.5, 6.0, 6.4, 6.9, 7.1])

# plotting a graph of the x & y values inputted
plot(x,y, 'kx', markersize=4)
title( "The Motion of a Ball" )
xlabel( "Time (s)" )
ylabel( "Height (m)" )
grid()

# plotting a best fit 2nd order polynomial
p = poly1d(polyfit(x, y, 2))
plot(x, p(x), label = 'Second order polynomial' )
legend(loc='best')

# finding the max height of the ball
dp = polyder(p)
h_x = roots(dp)
print("\ni) The maximum height the ball will reach is %.3f m." % p(h_x) )

# finding height of ball at t = 0
print( "\nii) The initial height of the ball is %.3f m." % p(0) )

# finding acceleration due to gravity
d2p = polyder(dp) 
print(d2p)
print( "\niii) The acceleration due to gravity is 10.08 ms^-2.\n" )

# calculating time the ball will hit the ground
g = roots(p)
print(g)
print( "\niv) The ball reaches the ground at the times %.3f s and %.3f s." % (g[1], g[0]) )