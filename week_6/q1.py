from pylab import *

# input x and y data
V, I = loadtxt( "data.txt", skiprows = 1, unpack = True)

# plotting data points on graph
plot( V, I, 'kx', markersize = 3, label = 'data' ) 

# add 1st order best fit line
p_coeff = polyfit( V, I, 1 ) 
p = poly1d( p_coeff ) 
x = linspace( min(V), max(V), 100 ) 
plot( x, p(x), label='Best Fit Line' )

# add x and y labels, title & legend
xlabel( 'Voltage (V)' ) 
ylabel( 'Current (A)' ) 
title( 'Voltage vs Current' )
legend( loc = 'best' )

# format graph
grid( ) 

# calculate errors
n = len( V )
D = sum( V**2 ) - 1./n * sum( V )**2
x_bar = mean(V)
p_coeff, residuals, _, _, _ = polyfit(V, I, 1, full=True)
dm_squared = 1./(n-2)*residuals/D 
dc_squared = 1./(n-2)*(D/n + x_bar**2)*residuals/D
dm = sqrt(dm_squared)
dc = sqrt(dc_squared)

# output file for data
f = open( "data.txt")
header = f.readline()
new_data = loadtxt(f)

# calculating resistance and its error
r = 1 / p_coeff[0]
dr = dm / p_coeff[0]**2

g = open("new_data.txt", 'w')
g.write(header)
g.write("The length of the data is %d" % len(V))
g.write("\nThe maxima and minima of the voltage (V) is %.3f and %.3f" % (max(V), min(V)) )
g.write("\nThe maxima and minima of the current (A) is %.3f and %.3f" % (max(I), min(I)) )
g.write("\nThe gradient is %.3f and its error is %.3f" % (p_coeff[0], dm) )
g.write("\nThe y-intercept is %.3f and its error is +/- %.3f" % (p_coeff[1], dc) )
g.write("\nThe resistance is %.3f and its error is +/- %.3f" % (r, dr) )
g.close()