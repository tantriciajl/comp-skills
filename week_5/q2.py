# input x and y data
x_data = input( "Please type in your x values with each value separated by a ,\n" )
x_data = array( x_data.split(',') , dtype = float )
y_data = input( "Please type in your y values with each value separated by a ,\n" )
y_data = array( y_data.split(',') , dtype = float )

# plot data on graph
plot( x_data, y_data, 'kx', markersize = 13, label = 'data' ) 

# add 1st order best fit line
p_coeff = polyfit( x_data, y_data, 1 ) 
p = poly1d( p_coeff ) 
x = linspace( min(x_data), max(x_data), 100 ) 
plot( x, p(x), label='Best Fit Line' )

# print y = mx + c
print( 'y = mx + c:')
print(p)

# input x and y labels 
x_label = input( "Please type in the label for your x-axis\n" )
xlabel( x_label ) 
y_label = input( "Please type in the label for your y-axis\n" )
ylabel( y_label ) 

# title & legend
title( 'Hookes Law' )
legend( loc = 'best' )

# format graph
grid( )

# calculate errors
n = len( x_data )
D = sum( x_data**2 ) - 1./n * sum( x_data )**2
x_bar = mean(x_data)
p_coeff, residuals, _, _, _ = polyfit(x_data, y_data, 1, full=True)
dm_squared = 1./(n-2)*residuals/D 
dc_squared = 1./(n-2)*(D/n + x_bar**2)*residuals/D
dm = sqrt(dm_squared)
dc = sqrt(dc_squared)

# print m, dm and c, dc
print( 'The gradient (mkg^-1) is %.3f and its error (mkg^-1) is %.3f' % (p_coeff[0], dm) )
print( 'The y intercept (m) is %.3f and its error (m) is %.3f' % (p_coeff[1], dc) )
