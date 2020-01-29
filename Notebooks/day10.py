import math

def main():


def return_angle(a, b, c):
	'''
	a, b, and c are 3 coordinate pairs that make up an angle, where b is the vertex. 
	Returns the angle made by these three points 
	'''
	# vectors that make up angle ABC
	ab = (a[0] - b[0], a[1] - b[1])
	cb = (c[0] - b[0], c[1] - b[1])

	# vector magnitudes
	mag_ab = math.sqrt(ab[0]**2 + ab[1]**2)
	mag_cb = math.sqrt(cb[0]**2 + cb[1]**2)

	# dot product of ab and cb
	ab_cb_dot = ab[0]*cb[0] + ab[1]*cb[1]

	# rearranging the dot product to get the angle, theta
	theta = math.acos(ab_cb_dot/(mag_ab*mag_cb))

	return theta


if __name__ == '__main__':
	main()