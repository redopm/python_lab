#!/usr/bin/python
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
''' this is for tell version of python
import os
print os.sys.version '''

# to find the current date and time 
'''
import commands
print "current date and time :"
print commands.getoutput("date") 

# to find area of circle given by radius

r=float(input("enter your radius:"))
print str(3.14 * (r**2)	)'''

# to print string with reverse order
'''a=raw_input("enter first & second name: ")
b=a.split(" ")
c=b.reverse()
d="".join(c)
d=b[::-1]
print d
print("enter your number for addition:")
a=input()
b=input()
print("your addition is",int(a)+int(b))
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

B = [[1, 4, 5, 12], 
    [-6, 7, 11, 19],
    [-5, 8, 9, 0]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

print("A =", A) 
print("B =", B)
#addition of a and b
print("addition of element a and b of matrix:", A[0][0]+B[0][0])
print("addition of element a and b of matrix:", A[0][1]+B[0][1])
print("addition of element a and b of matrix:", A[0][2]+B[0][2])
print("addition of element a and b of matrix:", A[0][3]+B[0][3])
for i in range(len(A)):
   # iterate through columns
   for j in range(len(A[0])):
       result[i][j] = A[i][j] + B[i][j]

for r in result:
   print(r)

print("lenth of A:", len(A))
print("A[0] =", A[0])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1]) # Last element of 1st Row'''
num=int(input("enter your rows:"))
for i in range(1, num+1):
	for j in range(1,i+1):
		print(end="")
	for j in range(i,0,-1):
		print(j)
	for j in range(2,i+1):
		print(j)
	print()