import matplotlib.pyplot as plt
from math import pi, cos, sin

def referentials():
	O = (0, 0, 0)
	X = (1, 0, 0)
	Y = (0, 1, 0)
	Z = (0, 0, 1)

	#plt.plot(X[0], X[1], X[2], marker='o', color='r')
	#plt.plot(Y[0], Y[1], Y[2], marker='o', color='g')
	#plt.plot(Z[0], Z[1], Z[2], marker='o', color='b')

	scale = 10
	plt.plot([O[0], X[0] * scale], [O[1], X[1] * scale], [O[2], X[2] * scale], color='r')
	plt.plot([O[0], Y[0] * scale], [O[1], Y[1] * scale], [O[2], Y[2] * scale], color='g')
	plt.plot([O[0], Z[0] * scale], [O[1], Z[1] * scale], [O[2], Z[2] * scale], color='b')


	plt.plot([O[0], X[0] * -scale], [O[1], X[1] * -scale], [O[2], X[2] * -scale], color='r', linestyle='dashed')
	plt.plot([O[0], Y[0] * -scale], [O[1], Y[1] * -scale], [O[2], Y[2] * -scale], color='g', linestyle='dashed')
	plt.plot([O[0], Z[0] * -scale], [O[1], Z[1] * -scale], [O[2], Z[2] * -scale], color='b', linestyle='dashed')

def translate_point(point, alpha, beta, gamma):
	return (point[0] + alpha, point[1] + beta, point[2] + gamma)

def rot_x_point(point, omega):
	xr = point[0]
	yr = point[1] * cos(omega) - point[2] * sin(omega)
	zr = point[1] * sin(omega) + point[2] * cos(omega)
	return (xr, yr, zr)

def rot_y_point(point, phi):
	xr = point[0] * cos(phi) + point[2] * sin(phi)
	yr = point[1]
	zr = point[2] * cos(phi) - point[0] * sin(phi)
	return (xr, yr, zr)

def rot_z_point(point, kappa):
	xr = point[0] * cos(kappa) - point[1] * sin(kappa)
	yr = point[0] * sin(kappa) + point[1] * cos(kappa)
	zr = point[2]
	return (xr, yr, zr)
def rot_point(point, omega, phi, kappa):
	x = point[0]
	y = point[1]
	z = point[2]
	xr = x * cos(phi) * cos(kappa) + y * (sin(omega) * sin(phi) * cos(kappa) - cos(omega) * sin(kappa)) \
		 + z * (cos(omega) * sin(phi) * cos(kappa) + sin(omega) * sin(kappa))

	yr = x * cos(phi) * sin(kappa) + y * (sin(omega) * sin(phi) * sin(kappa) + cos(omega) * cos(kappa)) \
		+ z * (cos(omega) * sin(phi) * sin(kappa) - sin(omega) * cos(kappa))

	zr = -x * sin(phi) + y * sin(omega) * cos(phi) + z * cos(omega) * cos(phi)

	return (xr, yr, zr)

def rot_point_comp(point, omega, phi, kappa):

	pr = (xr, yr, zr) = rot_x_point(point, omega) # X rotation first
	pr = rot_y_point(pr, phi) # Then Y rotation
	pr = rot_z_point(pr, kappa) # Z rotation for last (This is a norm)

	return pr

def cube(size):
	
	return[(-size, -size, -size), (size, -size, -size), (-size, size, -size), (size, size, -size),\
		(-size, -size, size), (size, -size, size), (-size, size, size), (size, size, size)]

def display_cube(vertices):
	"""
	plt.plot([vertices[0][0], vertices[1][0]], [vertices[0][1], vertices[1][1]], [vertices[0][2], vertices[1][2]], color='r')
	plt.plot([vertices[0][0], vertices[2][0]], [vertices[0][1], vertices[2][1]], [vertices[0][2], vertices[2][2]], color='g')
	plt.plot([vertices[1][0], vertices[3][0]], [vertices[1][1], vertices[3][1]], [vertices[1][2], vertices[3][2]], color='g')
	plt.plot([vertices[2][0], vertices[3][0]], [vertices[2][1], vertices[3][1]], [vertices[2][2], vertices[3][2]], color='r')

	plt.plot([vertices[4][0], vertices[5][0]], [vertices[4][1], vertices[5][1]], [vertices[4][2], vertices[5][2]], color='r')
	plt.plot([vertices[4][0], vertices[6][0]], [vertices[4][1], vertices[6][1]], [vertices[4][2], vertices[6][2]], color='g')
	plt.plot([vertices[5][0], vertices[7][0]], [vertices[5][1], vertices[7][1]], [vertices[5][2], vertices[7][2]], color='g')
	plt.plot([vertices[6][0], vertices[7][0]], [vertices[6][1], vertices[7][1]], [vertices[6][2], vertices[7][2]], color='r')

	plt.plot([vertices[0][0], vertices[4][0]], [vertices[0][1], vertices[4][1]], [vertices[0][2], vertices[4][2]], color='b')
	plt.plot([vertices[1][0], vertices[5][0]], [vertices[1][1], vertices[5][1]], [vertices[1][2], vertices[5][2]], color='b')
	plt.plot([vertices[2][0], vertices[6][0]], [vertices[2][1], vertices[6][1]], [vertices[2][2], vertices[6][2]], color='b')
	plt.plot([vertices[3][0], vertices[7][0]], [vertices[3][1], vertices[7][1]], [vertices[3][2], vertices[7][2]], color='b')
	"""

	# Méthode hyper_cube
	def wt(a):
		x = a
		poids = 0
		while x > 0:
			x = x & (x-1)
			poids += 1
		return poids
	
	dim = 3
	couleurs = ['', 'r', 'g', '' ,'b']
	for i in range(1<<dim):
		for j in range(i+1, 1<<dim):

			if wt(i ^ j) == 1:

				plt.plot([vertices[i][0], vertices[j][0]], [vertices[i][1], vertices[j][1]], [vertices[i][2], vertices[j][2]], color=couleurs[j - i])

				

def translate_cube(vertices, alpha, beta, gamma):
	new_cube = [(0, 0, 0)] * 8
	for i in range(8):
		new_cube[i] = translate_point(vertices[i], alpha, beta, gamma)
	return new_cube

def rotate_cube(vertices, omega, phi, kappa):
	new_cube = [(0, 0, 0)] * 8
	for i in range(8):
		new_cube[i] = rot_point_comp(vertices[i], omega, phi, kappa)
	return new_cube

def scale(point, sx, sy, sz):
	return (point[0] * sx, point[1] * sy, point[2] * sz)

def scale_cube(vertices, sx, sy, sz):
	new_cube = [(0, 0, 0)] * 8
	for i in range(8):
		new_cube[i] = scale(vertices[i], sx, sy, sz)
	return new_cube


def init_world():
	# Initialize a new Plotting window
	plt.figure(figsize=(10, 10))
	# Initializing 3D capabilities
	axes = plt.axes(projection="3d")
	# Setting axis properties
	axes.set_xlim(-10, 10) # X Axis graduation
	axes.set_ylim(-10, 10) # Y Axis graduation
	axes.set_zlim(-10, 10) # Z Axis graduation
	axes.set_xlabel('X') # X Axis label
	axes.set_ylabel('Y') # Y Axis label
	axes.set_zlabel('Z') # Z Axis label
	axes.xaxis.label.set_color('red') # X Axis color
	axes.yaxis.label.set_color('green') # Y Axis color
	axes.zaxis.label.set_color('blue') # Z Axis color
	axes.tick_params(axis='x', colors='red') # X Axis graduation color
	axes.tick_params(axis='y', colors='green') # Y Axis graduation color
	axes.tick_params(axis='z', colors='blue') # Z Axis graduation color
	# Display the 3D plotting window
	referentials() # Display the X, Y, Z Axis

def display_points():
	init_world()
	p1 = (4.0, 3.0, 2.0)
	plt.plot(p1[0], p1[1], p1[2], marker='o', color='pink')

	p1 = translate_point(p1, 0.0, 1.0, 1.0)
	plt.plot(p1[0], p1[1], p1[2], marker='o', color='pink')

	p = (4.0, 4.0, 4.0)
	plt.plot(p[0], p[1], p[2], marker='o', color='black')

	p_rot_x = rot_x_point(p, pi/4)
	plt.plot(p_rot_x[0], p_rot_x[1], p_rot_x[2], marker='o', color='red')

	p_rot_y = rot_y_point(p, pi/4)
	plt.plot(p_rot_y[0], p_rot_y[1], p_rot_y[2], marker='o', color='green')

	p_rot_z = rot_z_point(p, pi/4)
	plt.plot(p_rot_z[0], p_rot_z[1], p_rot_z[2], marker='o', color='blue')

	p_rot = rot_point(p, 0, 0, pi/4)
	plt.plot(p_rot[0], p_rot[1], p_rot[2], marker='+', color='orange')


	p_rot_comp = rot_point_comp(p, 0, pi/4, 0)
	plt.plot(p_rot_comp[0], p_rot_comp[1], p_rot_comp[2], marker='+', color='purple')
	plt.show()

def dispalay_cube_translation():
	init_world()
	test_cube = cube(3)
	display_cube(test_cube)

	test_cube_translation = translate_cube(test_cube, 1.0, 2.0, 3.0)
	display_cube(test_cube_translation)
	plt.show()

def dispalay_cube_rotation():
	init_world()
	test_cube = cube(3)
	display_cube(test_cube)

	test_cube_rotation = rotate_cube(test_cube, pi/4, pi/3, pi/2)
	display_cube(test_cube_rotation)

	plt.show()

def display_diff():
	init_world()
	test_cube = cube(3)
	#display_cube(test_cube)

	test_cube_translation_first = translate_cube(test_cube, 0.25, 0.5, 0.75)
	test_cube_translation_first = rotate_cube(test_cube_translation_first, pi/6, pi/4, pi/3)
	display_cube(test_cube_translation_first)

	test_cube_rotation_first = rotate_cube(test_cube, pi/6, pi/4, pi/3)
	test_cube_rotation_first = translate_cube(test_cube_rotation_first, 0.25, 0.5, 0.75)
	display_cube(test_cube_rotation_first)

	plt.show()

def display_scale():
	init_world()
	test_cube = cube(3)
	display_cube(test_cube)

	sx = 3.3
	sy = 3.3
	sz = 3.3
	test_cube_upscale = scale_cube(test_cube, sx, sy, sz)
	display_cube(test_cube_upscale)

	sx = 0.5
	sy = 0.5
	sz = 0.5
	test_cube_downscale = scale_cube(test_cube, sx, sy, sz)
	display_cube(test_cube_downscale)
	plt.show()



def main():
	display_points()
	dispalay_cube_translation()
	dispalay_cube_rotation()
	display_diff()
	display_scale()

	

	

	

	plt.show()
if __name__ == "__main__":
	main()