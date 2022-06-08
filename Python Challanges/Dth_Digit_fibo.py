#!/usr/bin/python

def common_decency(N):
	stringNum = str(N)
	threeCount = 0
	fiveCount = 0

	for num in stringNum:
		if num != "3" and num != "5":
			return False
		elif num == "3":
			threeCount += 1
		elif num == "5":
			fiveCount += 1
		
	if fiveCount % 3 == 0 and threeCount % 5 == 0:
			return True
			
	else:
		return False
		
print(common_decency(555))
			