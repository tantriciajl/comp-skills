# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:16:08 2020

@author: Tricia Tan
"""

from pylab import *

# create dataset using polynomial P(x)
p = poly1d([3, -4, -7, 1, 2, 10])

# create x-axis intervals
x = linspace(-1.5, 2.5, 5)
y = p(x)

# create output file to save answers
i = open("int_accuracy_answers.txt", 'w')


# integrate using polyint() method
q = polyint(p)
s= q(x)

int = s[-1] - s[0]

i.write("2)a) The theoretical integral of p(x) is %.3f.\n" % int )



"""4 intervals"""

i.write("\n4 intervals:\n")
        
# integrate using left rectangular method
dx = x[1] - x[0]
w_left = ones_like(y)
w_left[-1] = 0
w_left4 = dx * sum(w_left * y)

abs_rect4 = abs(w_left4 - int) # calculate absolute error

i.write("\nThe integral of p(x) using the left rectangular method is %.3f and its absolute error is %.3f.\n" % (w_left4, abs_rect4) )

# integrate using trapezium method
w_trap = ones_like(y)
w_trap[0] = 0.5
w_trap[-1] = 0.5
w_trap4 = dx * sum(w_trap * y)

abs_trap4 = w_trap4 - int # calculate absolute error

i.write("\nThe integral of p(x) using the trapezium method is %.3f and its absolute error is %.3f.\n" % (w_trap4, abs_trap4) )


# integrate using simpsons method
w_simp = ones_like(y)
w_simp[1:-1:2] = 4
w_simp[2:-1:2] = 2
w_simp = (1/3) * w_simp
w_simp4 = dx * sum(w_simp * y)

abs_simp4 = abs(w_simp4 - int)

i.write("\nThe integral of p(x) using the Simpson's method is %.3f and its absolute error is %.3f.\n" % (w_simp4, abs_simp4) )




"""8 intervals"""

# change intervals
x = x = linspace(-1.5, 2.5, 9)
y = p(x)

i.write("\n2)b) 8 intervals:\n")

# change dx
dx = x[1] - x[0]

# integrate using left rectangular method
w_left = ones_like(y)
w_left[-1] = 0
w_left8 = dx * sum(w_left * y)

abs_rect8 = abs(w_left8 - int) # calculate absolute error

i.write("\nThe integral of p(x) using the left rectangular method is %.3f and its absolute error is %.3f.\n" % (w_left8, abs_rect8) )

# integrate using trapezium method
w_trap = ones_like(y)
w_trap[0] = 0.5
w_trap[-1] = 0.5
w_trap8 = dx * sum(w_trap * y)

abs_trap8 = w_trap8 - int # calculate absolute error

i.write("\nThe integral of p(x) using the trapezium method is %.3f and its absolute error is %.3f.\n" % (w_trap8, abs_trap8) )


# integrate using simpsons method
w_simp = ones_like(y)
w_simp[1:-1:2] = 4
w_simp[2:-1:2] = 2
w_simp = (1/3) * w_simp
w_simp8 = dx * sum(w_simp * y)

abs_simp8 = w_simp8 - int

i.write("\nThe integral of p(x) using the Simpson's method is %.3f and its absolute error is %.3f.\n" % (w_simp8, abs_simp8) )



"""16 intervals"""

# change intervals
x = linspace(-1.5, 2.5, 17)
y = p(x)

i.write("\n16 intervals:\n")

# change dx
dx = x[1] - x[0]

# integrate using left rectangular method
w_left = ones_like(y)
w_left[-1] = 0
w_left16 = dx * sum(w_left * y)

abs_rect16  = abs(w_left16  - int) # calculate absolute error

i.write("\nThe integral of p(x) using the left rectangular method is %.3f and its absolute error is %.3f.\n" % (w_left16 , abs_rect16 ) )

# integrate using trapezium method
w_trap = ones_like(y)
w_trap[0] = 0.5
w_trap[-1] = 0.5
w_trap16  = dx * sum(w_trap * y)

abs_trap16  = w_trap16  - int # calculate absolute error

i.write("\nThe integral of p(x) using the trapezium method is %.3f and its absolute error is %.3f.\n" % (w_trap16 , abs_trap16 ) )

# integrate using simpsons method
w_simp = ones_like(y)
w_simp[1:-1:2] = 4
w_simp[2:-1:2] = 2
w_simp = (1/3) * w_simp
w_simp16  = dx * sum(w_simp * y)

abs_simp16  = w_simp16  - int

i.write("\nThe integral of p(x) using the Simpson's method is %.3f and its absolute error is %.3f.\n" % (w_simp16 , abs_simp16 ) )



"""32 intervals"""

# change intervals
x = linspace(-1.5, 2.5, 33)
y = p(x)

i.write("\n32 intervals:\n")

# change dx
dx = x[1] - x[0]

# integrate using left rectangular method
w_left = ones_like(y)
w_left[-1] = 0
w_left32 = dx * sum(w_left * y)

abs_rect32 = abs(w_left32 - int) # calculate absolute error

i.write("\nThe integral of p(x) using the left rectangular method is %.3f and its absolute error is %.3f.\n" % (w_left32, abs_rect32) )

# integrate using trapezium method
w_trap = ones_like(y)
w_trap[0] = 0.5
w_trap[-1] = 0.5
w_trap32 = dx * sum(w_trap * y)

abs_trap32 = w_trap32 - int # calculate absolute error

i.write("\nThe integral of p(x) using the trapezium method is %.3f and its absolute error is %.3f.\n" % (w_trap32, abs_trap32) )

# integrate using simpsons method
w_simp = ones_like(y)
w_simp[1:-1:2] = 4
w_simp[2:-1:2] = 2
w_simp = (1/3) * w_simp
w_simp32 = dx * sum(w_simp * y)

abs_simp32 = w_simp32 - int

i.write("\nThe integral of p(x) using the Simpson's method is %.3f and its absolute error is %.3f.\n" % (w_simp32, abs_simp32) )

# plot log of error vs log of interval 
x_int = log(array([4, 8, 16, 32])) 

y_rect = log( array([abs_rect4, abs_rect8, abs_rect16, abs_rect32]) ) # left rectangular method
y_trap = log( array([abs_trap4, abs_trap8, abs_trap16, abs_trap32]) ) # trapezium method 
y_simp = log( array([abs_simp4, abs_simp8, abs_simp16, abs_simp32]) ) # Simpson's method

figure()
plot(x_int,y_rect, 'rx')
plot(x_int,y_trap, 'bx')
plot(x_int,y_simp, 'gx')
xlabel("Number of Intervals")
ylabel("Errors")
title("Natural Logarithm of Errors and Number of Intervals")

# calculate straight best fit lines
p_coeff_rect = polyfit( x_int, y_rect, 1 )  # left rectangular method
p_rect = poly1d( p_coeff_rect ) 
x = linspace( min(x_int), max(x_int), 100 ) 
plot( x, p_rect(x), 'r', label='Best fit line for Left Rectangle Method' ) 

p_coeff_trap = polyfit( x_int, y_trap, 1 )  # trapezium method
p_trap = poly1d( p_coeff_trap ) 
x = linspace( min(x_int), max(x_int), 100 ) 
plot( x, p_trap(x), 'b', label='Best fit Line for Trapezium Method' ) 

p_coeff_simp = polyfit( x_int, y_simp, 1 )  # Simpson's method
p_simp = poly1d( p_coeff_simp) 
x = linspace( min(x_int), max(x_int), 100 ) 
plot( x, p_simp(x), 'g', label="Best fit Line for Simpson's Method" ) 
legend(loc='best')

i.write("\n2)d) The slope of the left rectangle best fit line is %.3f.\n" % p_rect[1])
i.write("\nThe slope of the trapezium best fit line is %.3f.\n" % p_trap[1])
i.write("\nThe slope of the Simpson's best fit line is %.3f.\n" % p_simp[1])

# calculate difference between expected value of n and calculated value of n
diff_rect = (1 - abs(p_rect[1])) * 100 / 1
diff_trap = (2 - abs(p_trap[1])) * 100 / 2 
diff_simp = (4 - abs(p_simp[1])) * 100 / 4

i.write("\n2)e) Estimated values of n:\n")
i.write("\n For the left rectangle method, n = %.2f. This is gives a percentage error of %.1f percent from the expected value of n = 1.\n" % (abs(p_rect[1]), diff_rect))
i.write("\n For the trapezium method, n = %.2f. This is gives a percentage error of %.1f percent from the expected value of n = 2.\n" % (abs(p_trap[1]), diff_trap))
i.write("\n For the Simpson's method, n = %.2f. This is gives a percentage error of %.1f percent from the expected value of n = 4.\n" % (abs(p_simp[1]), diff_simp))
i.close()
savefig("log_error_vs_interval.png")




