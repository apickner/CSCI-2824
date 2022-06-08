def mega_digit(N,k):
	n = str(N)
	num_sum = 0
	for eachChar in n:
		num_sum += int(eachChar)
	new_digit = num_sum * k
	
	if new_digit < 10:
		p = new_digit
	else:
		p = mega_digit(new_digit, 1)
	
	return p		

#	print(total)
#	return finalString
	
print(mega_digit(321, 3))
