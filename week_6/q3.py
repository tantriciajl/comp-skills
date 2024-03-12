# input matrix A and matric B numbers
x = input( "Please type in eight numbers with each value separated by a ,\n" )
x = array( x.split(',') , dtype = float )
A = matrix( [[x[0], x[1]], [x[2], x[3]]] )
B = matrix ( [[x[4], x[5]], [x[6], x[7]]] )

print("Matrix A is:")
print(A)
print("Matrix B is:")
print(B)
print("A^-1 is:")
print(A**-1)
print("B^-1 is:")
print(B**-1)
print("A * B is:")
print(A*B)
print("(AB)^-1 is:")
print((A*B)**-1)
print("B^-1 * A^-1 is:")
print((B**-1)*(A**-1))

A_val, A_vect = eig(A)
print("The eigenvalues for A are:")
print(A_val)
print("The eigenvectors for A are:")
print(A_vect)