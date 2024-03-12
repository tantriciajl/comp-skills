# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:43:03 2020

@author: tricia
"""
from pylab import *

# input data to be plotted
t, x = mgrid[0.:2.:.01, 0.:2.:.01]

# create plot (t, x ,y)
y = sin( (2*pi*x) + (2*pi*t) )
contourf(x,t,y,100 )
title( "sin( (2*pi*x) + (2*pi*t)" )
colorbar(label = "Amplitude" )
xlabel("x")
ylabel("t")

# 1D plot 
figure()
plot( x[t==0], y[t==0], label='t = 0' ) 
plot( x[t==0.25], y[t==0.25], label='t = 0.25' ) 
plot( x[t==0.5], y[t==0.5], label='t = 0.5' ) 
title( "Amplitude vs x at t=0, 0.25 and 0.5" )
legend( loc='best' ) 
xlabel( "x" )
ylabel( "Amplitude" )

# making a standing wave
figure()
s = sin( (2*pi*x) - (2*pi*t) ) + sin( (2*pi*x) + (2*pi*t) )
contourf( s, 100 )
title( "Standing Wave" )
colorbar(label = "Amplitude" )
xlabel( "x" )
ylabel("t")

# 1D plot of s
figure()
plot( x[t==0], s[t==0], label='t = 0' ) 
plot( x[t==0.25], s[t==0.25], label='t = 0.25' ) 
plot( x[t==0.5], s[t==0.5], label='t = 0.5' ) 
title( "Amplitude vs x at t=0, 0.25 and 0.5" )
legend( loc='best' ) 
xlabel( "x" )
ylabel( "Amplitude" )