# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:26:18 2020

@author: Tricia Tan :)
"""

# drawing grass
x_gr = arange(10)
y_gr = array([0, .05, 0, .05, 0, .05, 0, .05, 0, .05])
plot( x_gr, y_gr, 'g', linewidth=1, label='grass' )

# drawing mountains
x_mo = arange(10)
y_mo = uniform(0.1, 1.0, 10)
plot( x_mo, y_mo, linewidth=1, label='mountains' )

# drawing birds
x_bi = uniform(0, 3, 30)
y_bi = uniform(max(y_mo), 1.3, 30)
plot( x_bi, y_bi, 'kx', markersize=2, label='birds' )

# drawing sun
x_su = 8
y_su = uniform(max(y_mo), 1.2) 
plot( x_su, y_su, 'yo ', markersize=42, label='sun' )