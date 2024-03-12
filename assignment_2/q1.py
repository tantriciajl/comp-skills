# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:29:21 2020

@author: Tricia Tan
"""

from pylab import *

# a) read in whole dataset
temp_data = loadtxt( "wales_temp.txt", skiprows=8)

# a)i) separate 'year' data
year = temp_data[0:,0]
year.flatten()

# a)ii) separate 'annual average temperature' data
ann_temp = temp_data[0:,17]
ann_temp.flatten()

# a)iii) separate 'monthly average temperature' data
mon_temp = temp_data[:,1:13]
print(mon_temp)

# create file to write in answers
w = open("wales_temp_info.txt", 'w')

# b)i) find highest monthly temperature
w.write("b)i) The highest monthly average temperature is %.2f degrees celsius.\n" % mon_temp.max() )

# b)ii) find the number of months when temperature was below zero
bel_zero = mon_temp[mon_temp<0]
w.write("\nb)ii) The number of months for which the average temperature was below zero is %d months.\n" % size(bel_zero) )


# b)iii) compare october's max temperature to august's lowest temperature
oct_max = max(mon_temp[:,9])
aug_min = min(mon_temp[:,9])

w.write("\nb)iii) October's highest monthly average temperature was %.2f degrees celsius and August's lowest monthly average temperature was %.2f degrees celsius. The hottest October had a higher temperature than the coolest August.\n" % (oct_max, aug_min))


# b)iv) find average temperature for each month
avg_mon_temp = sum(mon_temp, axis = 0) / 105
w.write("\nb)iv) The warmest month is June with an average temperature of %.2f degrees celsius. The coldest month is January with an average temperature of %.2f degrees celsius.\n" % ( avg_mon_temp[argmax(avg_mon_temp)], avg_mon_temp[argmin(avg_mon_temp)])  )


# c)i) find min and max annual temperature
w.write("\nc)i) The highest average annual temperature is %.2f degrees celsius in %d.\n" % (ann_temp[argmax(ann_temp)], year[argmax(ann_temp)]) )
w.write("\nThe lowest average annual temperature is %.2f degrees celsius in %d.\n" % (ann_temp[argmin(ann_temp)], year[argmin(ann_temp)]) )


# c)ii) plot histogram of average annual temperatures
hist(ann_temp, bins = 6, alpha=0.4, label="From 1911 to 2015")
xlabel('Annual Average Temperature (degrees celsius)')
title('Annual Average Temperature From 1911 to 2015')
grid()
hist(ann_temp[year>=1990], bins = 6, alpha=0.4, label="From 1990 to 2015")
title('Annual Average Temperature From 1990 to 2015')
legend(loc='best')

savefig('ann_temp_hist.png')

# c)iii) check if average temperature is increasing
w.write("\nc)iii) Yes because the figure shows the average annual temperature change from a positive skew between 1911 and 2015 to a negative skew between 1990 and 2015.\n" )

# c)iv) plot average temperature vs year graph
figure(), 
plot(year, ann_temp, 'kx')
xlabel('Year')
ylabel('Annual Average Temperature (degrees celsius)')
title('Annual Average Temperature From 1911 and 2015')

# create straight best fit line
p_coeff = polyfit( year, ann_temp, 1 ) 
p = poly1d( p_coeff ) 
x = linspace( min(year), max(year), 100 ) 
plot( x, p(x), label='Best Fit Line' ) 
legend(loc='best')

savefig('ann_temp_scatter.png')

m = p_coeff[0] # slope
c = p_coeff[1] # intercept

# calculate errors in straight best fit line
n = len(year)
D = sum(year**2) - 1./n * sum(year)**2
x_bar = mean(year)
p_coeff, residuals, _, _, _ = polyfit(year, ann_temp, 1, full=True)

dm_squared = 1./(n-2)*residuals/D 
dc_squared = 1./(n-2)*(D/n + x_bar**2)*residuals/D

# state straight best fit line equation w/ errors
w.write("\nc)iv) The slope is %.2f +\- %.2f degrees celsius per year.\n" % (m, sqrt(dm_squared)) )
w.write("\nThe intercept is is %.2f +\- %.2f degrees celsius.\n" % (c, sqrt(dc_squared)) )

# c)v) find average annual icrease/decrease in temperature
w.write("\nc)v) The average annual increase in temperature is %.2f +\- %.2f degrees celsius per year.\n" % (m, sqrt(dm_squared)) )
w.close()
