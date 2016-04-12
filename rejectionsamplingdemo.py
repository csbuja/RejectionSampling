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
	dist_from_center_x = abs(.5-x) 
	dist_from_center_y = abs(.5-y)
#	p = (dist_from_center_x,dist_from_center_y)
	p =(x,y)
	if (dist_from_center_x**2 + dist_from_center_y**2)**.5 <=.5:
		number_in_circle +=1
		pairs_in_circle.append(p)
	else:
		pairs_out_of_circle.append(p)
	i+=1

print "area between circle and square: " + str((max_iter-number_in_circle)/max_iter)


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
#plt.savefig('distanceplot.png')
