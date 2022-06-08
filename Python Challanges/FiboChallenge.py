def fibR(n):
	if n==1 or n==2:
		return 1
	return fibR(n-1)+fibR(n-2)
	
def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

def first_D_digit_Fib(D):
	fibo = 1
	a,b = 1, 1
	if D == 1: 
		return 0
	else:
		while fibo < 10**(D-1):
			a, b = b, a+b
			fibo = b

		return fibo
		
		


print(first_D_digit_Fib(3))
print(first_D_digit_Fib(2))