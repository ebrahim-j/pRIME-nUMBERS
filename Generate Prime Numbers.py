def isPrime(n):
	if n == 1 :
		return True
	elif n % 2 == 0:
		return False
	else:
		for i in range(3,n + 1,2):
			if n % i == 0:
				return False
			else:
				return True



def GeneratePrime(n):
	n = int(input("Insert here: "))
	for i in range(n+1):
		if isPrime(i) == True:
			print(i)

