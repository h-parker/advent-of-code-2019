import math

def main():
	og_map = """.#..#
				.....
				#####
				....#
				...##"""
	print(make_asteroid_map(og_map))
	

def make_asteroid_map(og_map):
	'''
	Given the original map (og_map), creates a new map that just lists the 
	coordinates of the asteroids
	'''
	asteroid_map = []
	y = 0
	x = 0

	for row in og_map.replace('\t', '').split('\n'):
		for element in row:
			print(element, x, y)
			if element == '#':
				asteroid_map.append((x, y))
			x += 1
		y += 1
		x = 0
		

	return asteroid_map

def num_visible_asteroids(asteroid_map, curr_asteroid):
	'''
	Returns the number of asteroids visible on asteroid_map from curr_asteroid 
	(given as coordinates).
	'''
	
	for asteroid in asteroid_map:
		pass



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