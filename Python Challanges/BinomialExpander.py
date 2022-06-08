import math 

def powerString(char, power):
	finalString = "(" + str(char)
	if power > 0:
		if power != 1:
			finalString += "^"
			finalString += str(power) + ")"
		else:
			finalString += ")"
	else:
		return ""
	return finalString


def binom_product(a,b,n):
	x = a
	y = b
	coefficient_list = list()
	
	i = 0
	while i <= n:
		coefficient = int((math.factorial(n))/(math.factorial(i)*math.factorial(n-i)))
		coefficient_list.append(coefficient)
		i += 1
	placeholder_x = n
	placeholder_y = 0
#	print(coefficient_list)
	finalString = ""
	for i in range(0,len(coefficient_list)):
		coefficient_list[i] *= (x)**(placeholder_x)
		coefficient_list[i] *= (y)**(placeholder_y)
		if i != 0 and coefficient_list[i] > 0:
			finalString += "+"
		finalString += str(coefficient_list[i])+powerString("x", placeholder_x)+powerString("y", placeholder_y)
		placeholder_x -= 1
		placeholder_y += 1
#	print(coefficient_list)
	return finalString
	

print(binom_product(3, -5, 4))q