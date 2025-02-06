import numpy as np
import cv2 as cv
import glob
import matplotlib.pyplot as plt

def calibrate_chessboard(image_files):
	image_width = -1
	image_height = -1
	# Arrays to store object points and image points from all the images.
	points_2d = [] # 2d points in image plane
	points_3d = [] # 3d point in real world space

	# Chessboard dimension
	rows = 9
	cols = 5
	size = 1.0

	objp = np.zeros((rows * cols, 3), np.float32)

	for x in range(0, cols):
		for y in range(0, rows):
			objp[y * cols + x] = [x * size, y * size, 0]

	
	print('Image list:')
	for image_file in image_files:
		print(' -'+image_file)

		# Load image
		img = cv.imread(image_file)

		# Get the image dimension
		(h, w) = img.shape[:2]

		if image_width == -1 and image_height == -1:
			image_width = w
			image_height = h
		
		elif w != image_width or h != image_height:
			print('All calibration images have to got same dimension, ignoring' + image_file)
			continue

		# Convert image to gray
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

		# Display image

		#plt.imshow(img, cmap='gray')
		#plt.show()
		# Find the chess board corners
		ret, corners = cv.findChessboardCorners(gray, (cols, rows), None)

		# If found, add object points, image points (after refining them)
		if ret is True:

			#Display image with corners
			plt.imshow(img, cmap='gray')

			#for corner in corners:
			#	plt.plot(corner[0][0], corner[0][1], marker='+', color='red')
			
			#plt.show()

			# termination criteria
			criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30,
			0.001)

			corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
			# Update 2D / 3D corner coordinates
			points_3d.append(objp)
			points_2d.append(corners2)

			# Display image with corners
			plt.imshow(img, cmap='gray')
			for corner in corners2:
				plt.plot(corner[0][0], corner[0][1], marker='+', color='red')
			#print(image_file, len(points_3d))
			#print(image_file, len(points_2d))
			#plt.show()

		
		else:
			print('No chessboard corner found on image ' + image_file)
			plt.imshow(img, cmap='gray')

			plt.show()

		
		#plt.show()
	
	print('Calibrating camera...', end='')
	camera_matrix = np.zeros((3, 3, 1), np.float32)
	dist_coefs = np.zeros((5, 1, 1), np.float32)
	retval, camera_matrix, dist_coefs, rvecs, tvecs = \
		cv.calibrateCamera(points_3d, points_2d,\
				(image_height, image_width), camera_matrix, dist_coefs)
	
	#print(retval, camera_matrix, dist_coefs, rvecs, tvecs)

	f_u = camera_matrix[0][0]
	print("f_u = ", f_u)
	f_v = camera_matrix[1][1]

	c_u = camera_matrix[0][2]
	c_v = camera_matrix[1][2]

	p_w = 1.4  / 1000 # en mm
	#ph = /image_height

	f = f_u * p_w

	print()
	print('focal length : ', f)

		
	# f : 28 mm
	


def main():

	# Load images from data folder
	image_files = glob.glob('data/images_iphone/*.jpg')
	
	calibrate_chessboard(image_files)

if __name__ == "__main__":
	main()