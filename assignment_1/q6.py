# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:35:31 2020

@author: Tricia Tan :)
"""

# inputting data
time, height = loadtxt( "skydive.txt", skiprows=1, unpack=True)

# plotting data
plot( time, height, 'kx', markersize=0.5 )

# creating output file
f = open("skydive answers.txt", 'w')
print(f)

# time at terminal velocity
f.write( "b)i) The skydiver reaches terminal velocity at around 5 seconds.\n" )

# time when parachute opens
f.write( "\nb)ii) The skydiver opens her parachute at around 25 seconds.\n" )

# calculating terminal velocity w/o parachute
term_t = time[19:100] # isolating data points within terminal velocity
term_h = height[19:100]

p_coeff = polyfit( term_t, term_h, 1 ) # creating 1st order polynomial
p = poly1d( p_coeff ) 
x = linspace( 5, 25, 100 ) 
plot( x, p(x), label='1st Order Polynomial (Without Parachute)' ) # plotting 1st order polynomial
term_v = polyder(p)
print(term_v)

# calculating terminal velocity error w/o parachute
n = len(term_t)
D = sum(term_t**2) - 1./n * sum(term_t)**2
p_coeff, residuals, _, _, _ = polyfit(term_t, term_h, 1, full=True)
dm_squared = 1./(n-2)*residuals/D

f.write( "\nc) The terminal velocity of the skydiver without the parachute is 52.86 +/- %.2f ms^-1.\n" % sqrt(dm_squared) )

# calculating terminal velocity w/ parachute
pterm_t = time[99:200]
pterm_h = height[99:200]
pp_coeff = polyfit( pterm_t, pterm_h, 1 ) # creating 1st order polynomial
pp = poly1d( pp_coeff )
px = linspace( 25, 50, 100 ) 
plot( px, pp(px), label='1st Order Polynomial (With Parachute)' ) # plotting 1st order polynomial
pterm_v = polyder(pp)
print(pterm_v)

# calculating terminal velocity error w/ parachute
pn = len(pterm_t)
pD = sum(pterm_t**2) - 1./pn * sum(pterm_t)**2
pp_coeff, presiduals, _, _, _ = polyfit(pterm_t, pterm_h, 1, full=True)
pdm_squared = 1./(pn-2)*presiduals/pD

f.write( "\nd) The terminal velocity of the skydiver with the parachute open is 8.07 +/- %.2f ms^-1.\n" % sqrt(pdm_squared) )

# calculating accelerating of diver
v = term_v
u = pterm_v
t = 1
a = (v-u)/t
print(a)
f.write( "\ne) The average acceleration during that time is 44.78 ms^-2.\n")

# caculating landing time
f.write( "\nf) The skydiver is expected to land on the ground at %.2f s.\n" % roots(pp) )

# calculating range of landing times
pp_min = poly1d( [(-8.072 - sqrt(pdm_squared)), pp_coeff[1]] ) # varied terminal speed to max and min errors in part d) 
pp_max = poly1d( [(-8.072 + sqrt(pdm_squared)), pp_coeff[1]] )
f.write( "\nThe range of possible landing times vary between %.2f and %.2f s." % ( roots(pp_min), roots(pp_max) ) )

# formatting graph
title( "A Skydiver's Descent" )
xlabel( "Time (s)" )
ylabel( "Height above ground (m)" )
legend(loc = 'best')
grid()

# saving graph and text
savefig("skydive")
f.close()




