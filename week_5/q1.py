# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# input string
name = input("Please type in your name\n")
print("Hello %s" % name)

# create float array
data = input( "Please type in three numbers with each number separated by a ,\n" )
data = array( data.split(',') , dtype = float )
print(data)

# create output file
f = open( "week 5.txt ", 'w' )
print(f)

# write original string
f.write(name)

# write string in uppercase
f.write(name.upper())

# write letters before letter e
e = name.split('e')
f.write(e[0])

# write float array
f.write(" %d\n" % data[0])
f.write(" %.2f\n" % data[1])
f.write(" %.3e\n" % data[2])

f.close()