# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:29:23 2020

@author: Tricia Tan :)
"""
# creating vectors
x = array([-4.18, 4.60, 5.16])
y = array([-3.47, 3.40, 1.07])
z = array([-4.04, 4.22, 5.59])
a = array([5.46, 4.61, 3.06])
b = array([-5.12, 5.82, -2.24])
c = array([25.55, -25.90, -22.65])
d = array([-1.63, 0.69, 4.88])

# comparing lengths to x
print(norm(x)==norm(a))
print(norm(x)==norm(b))
print(norm(x)==norm(c))
print(norm(x)==norm(d))
print( "\ni) None of the vectors have the same length as x.\n" )

# finding vector perpendicular to y
print( dot(y,a) )
print( dot(y,b) )
print( dot(y,c) )
print( dot(y,d) )   
print( "\nii) a is perpendicular to y.\n")

# finding vectors in the same plane as x and y
t = cross(x,z)
print( dot(t,a) )
print( dot(t,b) )
print( dot(t,c) )
print( dot(t,d) )
print( "\niii) d lies in the same plane as x and z.\n" )


# finding y + z
s = y + z 
print( cross(s,a) )
print( cross(s,b) )
print( cross(s,c) )
print( cross(s,d) )
print( "\niv) c is parallel to y + z.\n" )