# input data
x = loadtxt("two_gauss.txt")

# size of data
print("The number of data points is %d" % len(x))

# plot histogram
hist( x, bins = 100 )

# format histogram
title("Two Gaussian Distributions")
xlabel("x")
ylabel("y")
grid()

# data is split between 5

# sample size of left & right distribution
x_left = x[x < 5]
print("The number of samples in the left gaussian distribution is %d" % len(x_left))

x_right = x[x>=5]
print("The number of samples in the right gaussian distribution is %d" % len(x_right))

# mean of left and right distribution
x_left_mean = mean(x_left)
print("The mean of the left gaussian distribution is %.3f" % x_left_mean)

x_right_mean = mean(x_right)
print("The mean of the right gaussian distribution is %.3f" % x_right_mean)

# SD of left and right distribution
left_sd = std(x_left)
print("The standard deviation of the left gaussian distribution is %.2f" % left_sd )

right_sd = std(x_right)
print("left %.2f The standard deviation of the right gaussian distribution is %.2f" %(left_sd, right_sd ))