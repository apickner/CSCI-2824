import math

def wrangle_rectangles(m,n):
	rectangles = 0
	if (n == 1 or m == 1):
		if (n == 1):
			rectangles = int(math.fsum(range(1,m+1)))
			return rectangles
		elif (m == 1):
			rectangles = int(math.fsum(range(1,n+1)))
			return rectangles
		else:
			return 1
	else:
		n_holder = int(math.fsum(range(1, n+1)))
		m_holder = int(math.fsum(range(1, m+1)))
		return n_holder * m_holder