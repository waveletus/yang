##########################################################
#Draw 3D geometry such as cubic and tetrahedron
#The algorithms depends on if there are a flat on the top
#If there is a top, then two points extends outside
#Otherwise it is one point extended
##########################################################

import sys
import numpy as np 
from numpy.linalg import inv



sides = []
top = []
bottom = []

def get_side_hedron(totalsides, downlength, height):
	temp = []
	angle = np.arctan(height/(downlength/2))
	temp.append((0, 0))
	temp.append((downlength/2, height))
	temp.append((downlength,0))
	sides.append(temp)
	for i in range(1, totalsides):
		new_point = sides[-1][0:2]
		update_point = sides[-1][-1]
		for j in range(0,i):
			update_point = retropect(angle, downlength, update_point)
		new_point.append(update_point)
		sides.append(new_point)

	

def get_side_cubic(totalsides, downlength, uplength, height):
	temp = []
	angle = np.arctan(height/(downlength-uplength)/2)
	temp.append((0,0))
	temp.append(((downlength-uplength)/2, height))
	temp.append(((downlength+uplength)/2, height))
	temp.append((downlength,0))
	for i in range(1, totalsides):
		new_point = sides[-1][0:2]
		update_point = sides[-1][2:4]
		for point in update_point:
			for j in range(0, i):
				point = retropect(angle, downlength, point)
			new_point.append(point)
	draw_output(new_point)


def retropect(alpha, position, point):
	matrix_return = np.array([-1*np.cos(alpha), np.sin(alpha)], [-1*np.sin(alpha), np.cos(alpha)])
	newvector = np.array([point[0], point[1]])
	inverse_matrix = inv(matrix_return)
	temp = inverse_matrix.dot(newvector)
	temp = temp + np.array([position, 0])
	return(set(temp[0], temp[1]))

def get_top(flag, totalsides,downlength):
	result = []
	alpha = (2*math.pi)/totalsides
	r = (downlength/2)/np.sin(alpha/2)
	angle = []
	angle.append(-1*alpha/2 - math.pi/2)
	for i in range(1, totalsides):
		angle.append(angle[-1] + alpha)
	if flag == 1:
		coordinate = [downlength/2, (downlength/2)/np.tan(alpha/2) ]

	if flag == -1:
		coordinate = [downlength/2, -1*(downlength/2)/np.tan(alpha/2)]

	for itm in angle:
		tmpx = r*np.cos(itm) + coordinate[0]
		tmpx = r*np.sin(itm) + coordinate[1]
		result.append((tmpx, tmpy))
	return(result)

def draw_output():
	pass

def main():
	get_side_hedron(3, 8, 10);
	get_top(1, 3, 8)
	draw_output()

	











