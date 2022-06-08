import math

def C(n,r):
	newN = math.factorial(n)
	newR = math.factorial(r)
	difference = n - r
	if (difference < 0):
		return 0
	quotient = int((newN)/((newR)*math.factorial(difference)))
	return quotient

def treasure_hunt(m,n,p):
	mxn = m*n
	################################################	
	# if the knight and chest are on same spot
	chestKnight = C(mxn, 1)
	dragon1 = C((mxn - 1), p)
	
	product1 = chestKnight * dragon1
		
	################################################	
	# if the knight and chest are NOT on same spot
	chest = C(mxn, 1)
	knight = C((mxn - 1), 1)
	dragon2 = C((mxn - 2), p)
	
	product2 = chest * knight * dragon2
	
	
	return product1 + product2
	
print(treasure_hunt(2, 1, 1)) # works!!!
print(treasure_hunt(2, 2, 1)) # works!!!
print(treasure_hunt(3, 4, 2)) # works!!!
