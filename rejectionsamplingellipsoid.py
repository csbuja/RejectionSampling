#USING EQUATIONS FROM CONVEX OPTIMIZATION BOOK
import numpy as np

def isInEllipse(p):
	x = np.array([[v for v in p]])
	x_center = np.array([[.5,.5]])

	P_inverse = np.linalg.inv(np.matrix(np.array([[.01,0],[0,.2]])))
	z = np.matrix(x-x_center).T  # is a column vector
	return z.T*P_inverse*z <=1




import random as r
r.seed(2)
import matplotlib.pyplot as plt

max_iter = 100000
number_in_circle = 0.0
pairs_in_circle = []
pairs_out_of_circle = [] 

i=0
while i<max_iter:
	x = r.random()
	y = r.random()

	p =(x,y)
	if isInEllipse(p):
		number_in_circle +=1
		pairs_in_circle.append(p)
	else:
		pairs_out_of_circle.append(p)
	i+=1

print "area between ellipse and square: " + str((max_iter-number_in_circle)/max_iter)


in_circle_x=[]
in_circle_y=[]
out_circle_x=[]
out_circle_y=[]
assert((len(pairs_in_circle)+len(pairs_out_of_circle)) == max_iter)
for in_ in pairs_in_circle:
	in_circle_x.append(in_[0])
	in_circle_y.append(in_[1])

for out_ in pairs_out_of_circle:
	out_circle_x.append(out_[0])
	out_circle_y.append(out_[1])
x = in_circle_x + out_circle_x
y = in_circle_y+ out_circle_y
assert(len(in_circle_y)+ len(out_circle_y) == max_iter)
colors = ['blue']*int(number_in_circle) + ['red']*int(max_iter-number_in_circle)
plt.scatter(x,y,c=colors,marker='x')
plt.show()
# plt.savefig('ellipse.png')
