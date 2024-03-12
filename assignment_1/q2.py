# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:12:29 2020

@author: Tricia Tan :)
"""

# generating 100,000 repetitions of 10 tosses
n = normal(loc = 5, size = 100000)

# making histogram
hist(n, bins = 25, range = (0,10))
xlabel("Number of heads in 10 tosses")
ylabel("Frequency")
title("100,000 Repetitions of 10 Tosses of a Fair Coin")

# calculating mean and SD
print( "\nii) The mean number of heads is %.3f." % mean(n) )
print( "\nThe standard deviation is %.3f." % sqrt(var(n)) )

# calculating probabillity of getting 7 or more heads
print( "\niii) The probability of getting 7 or more heads is %.3f." % (sum(n>=7)/100000) )
print( "\nAlthough unlikely, the distribution shows there is still a small probability of getting 7 heads out of 10 tosses, so I wouldn't think the coin is unfair." )

# generating 100,000 repetitions of 100 tosses
s = normal(loc = 50, size = 100000)

# making histogram
figure()
hist(s, bins = 1000, range = (0,100))
xlabel("Number of heads in 100 tosses")
ylabel("Frequency")
title("100,000 Repetitions of 100 Tosses of a Fair Coin")

# calculating probability of getting 70 or more heads
print( "\niv) The probability of getting 70 or more heads is %.3f." % (sum(s>=70)/100000) )
print( "\nI would think the coin is biased because the probability of getting 70 heads out of 100 tosses is extremely unlikely, the distribution shows that it's pretty much impossible." )