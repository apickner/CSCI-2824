import math 

def binom_product(a,b,n):
	x = a
	y = b
	coefficient_list = list()
	
	i = 0
	while i <= n:
		coefficient = (math.factorial(n))/(math.factorial(i)*math.factorial(n-i))
		coefficient_list.append(coefficient)
		i += 1
	placeholder_x = n
	placeholder_y = 0
	total = 1
	print(coefficient_list)
	for i in range(0,len(coefficient_list)):
		coefficient_list[i] *= (x)**(placeholder_x)
		coefficient_list[i] *= (y)**(placeholder_y)
		total *= coefficient_list[i]
		placeholder_x -= 1
		placeholder_y += 1
#	print(coefficient_list)
	
	return total
	
print(binom_product(2, -1, 3))