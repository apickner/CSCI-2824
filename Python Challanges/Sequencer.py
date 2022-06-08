def sequence_slayer(N):
	a0 = 1
	a1 = 2
	aN = 0
	if N == 0:
		return a0
	elif N == 1:
		return a1
	
	else:
		n = 2
		for i in range(N):
			aN = n**(2)*(a1)-(a0)
			n += 1
			a0 = a1
			a1 = aN
			
		return aN
		
print(sequence_slayer(2))