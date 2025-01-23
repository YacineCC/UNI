import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin
from transfos_referentials import init_world, cube, display_cube


# EX 1
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])

print('a = ', a, 'b = ', b)
print("a+b = ", a+b)
print('a-b = ', a-b)
print('a*b = ', a*b)
print('a.b = ', a.dot(b))
print('axb = ', np.cross(a, b))
print()

# EX 2
M = np.array(((0, 0, 1), (0, 1, 0), (0, 1, 1)))
print(M)
print()

# EX 3

R = np.array(((1, 0, 0), (0, 2, 0), (0, 0, 3)))
V = np.array([4, 5, 6])
print("R = ", R)
print("V = ", V)
print("R.V = ", R.dot(V))
print()

#EX 4
M = np.array(((1, 0, 0, 1), (0, 2, 0, 4), (0, 0, 3, 1)))
K = np.array(((4, -1), (3, 2), (2, -5), (6, 4)))

print("M = ", M)
print('K = ', K)
print('M.K = ', M.dot(K))
print()

#EX 5

def toHomogeneous(v : tuple[float]) -> np.array:
	return np.array([v[0], v[1], v[2], 1])
print(toHomogeneous((1.0, 2.0, 3.0)))
print()
#EX 6

def toEuclidean(v : tuple[float]) -> np.array:
	return (np.array([v[0], v[1], v[2]]) / v[3])
print(toEuclidean((2.0, 4.0, 6.0, 2.0)))
print()

#EX 7
def translate_point(point : np.array,\
	 alpha : float, beta : float, gamma : float)\
		 -> np.array:

	translation_matrix = np.array(((1, 0, 0, alpha),\
		 						(0, 1, 0, beta),\
								(0, 0, 1, gamma),\
								(0, 0, 0, 1)))
	p = toHomogeneous(point)

	return toEuclidean(translation_matrix.dot(p))


print(translate_point((4.0, 3.0, 2.0), 0.0, 1.0, 1.0))

#EX 8
def rot_x_point(point, omega : float):

	rot_x_matrix = np.array(((1, 0, 0, 0),\
							(0, cos(omega), -sin(omega), 0),\
							(0, sin(omega), cos(omega), 0),\
							(0, 0, 0, 1)))
	
	p = toHomogeneous(point)

	return toEuclidean(rot_x_matrix.dot(p))


init_world()
p1 = (4.0, 4.0, 4.0)
plt.plot(p1[0], p1[1], p1[2], marker='o', color='black')

# Rotation sur X
p1_rx = rot_x_point(p1, pi/4)
plt.plot(p1_rx[0], p1_rx[1], p1_rx[2], marker='o', color='red')


# EX 9
def rot_y_point(point, phi):
	rot_y_matrix = np.array(((cos(phi), 0, sin(phi), 0),\
							(0, 1, 0, 0),\
							(-sin(phi), 0, cos(phi), 0),\
							(0, 0, 0, 1)))
	p = toHomogeneous(point)
	return toEuclidean(rot_y_matrix.dot(p))

# Rotation sur Y
p1_ry = rot_y_point(p1, pi/4)
plt.plot(p1_ry[0], p1_ry[1], p1_ry[2], marker='o', color='green')


# EX 10
def rot_z_point(point, kappa):
	rot_z_matrix = np.array(((cos(kappa), -sin(kappa), 0, 0),\
							(sin(kappa), cos(kappa), 0, 0),\
							(0, 0, 1, 0),\
							(0, 0, 0, 1)))
	p = toHomogeneous(point)
	return toEuclidean(rot_z_matrix.dot(p))

# Rotation sur Z
p1_rz = rot_z_point(p1, pi/4)
plt.plot(p1_rz[0], p1_rz[1], p1_rz[2], marker='o', color='blue')


#EX 11
def rot_point(point, omega, phi, kappa):

	return rot_z_point(rot_y_point(rot_x_point(point, omega), phi), kappa)

#Rotation globale
p1_rgx = rot_point(p1, pi/4, 0, 0)
p1_rgy = rot_point(p1, 0, pi/4, 0)
p1_rgz = rot_point(p1, 0, 0, pi/4)
plt.plot(p1_rgx[0], p1_rgx[1], p1_rgx[2], marker='+', color='white')
plt.plot(p1_rgy[0], p1_rgy[1], p1_rgy[2], marker='+', color='white')
plt.plot(p1_rgz[0], p1_rgz[1], p1_rgz[2], marker='+', color='white')

plt.show()
init_world()
test_cube = cube(3)
display_cube(test_cube)

#EX 12
def translate_cube(vertices, alpha, beta, gamma):
	new_cube = [(0, 0, 0)] * 8
	for i in range(8):
		new_cube[i] = translate_point(vertices[i], alpha, beta, gamma)
	return new_cube
translation_cube = translate_cube(test_cube, 1.0, 2.0, 3.0)
display_cube(translation_cube)

#EX 13
def rotate_cube(vertices, omega, phi, kappa):
	new_cube = [(0, 0, 0)] * 8
	for i in range(8):
		new_cube[i] = rot_point(vertices[i], omega, phi, kappa)
	return new_cube

rotation_cube = rotate_cube(test_cube, pi/4, pi/3, pi/2)
display_cube(rotation_cube)

plt.show()

#EX 14
init_world()
test_cube_2 = cube(2)

scale = 10
alpha = 0.25 * scale
beta = 0.5 * scale
gamma = 0.75 * scale

kappa = pi/3
phi = pi/4
omega = pi/6

merge_transfo_cube_1 = translate_cube(test_cube_2, alpha, beta, gamma)
merge_transfo_cube_1 = rotate_cube(merge_transfo_cube_1, kappa, phi, omega)
display_cube(merge_transfo_cube_1)

merge_transfo_cube_2 = rotate_cube(test_cube_2, kappa, phi, omega)
merge_transfo_cube_2 = translate_cube(merge_transfo_cube_2, alpha, beta, gamma)
display_cube(merge_transfo_cube_2)

# The order of the transformations matter even if the values
# of the translation vector et and the angles are the same.
# the bigger the translation the more it shows.

plt.show()