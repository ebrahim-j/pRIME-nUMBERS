def isPrime(n):
	if n == 1 || n==2 || n==3 :
		return True
	#checks if number is even(even numbers are not prime)
	elif n % 2 == 0:
		return False
	elif n > 2:
		#looping through odd numbers
		for i in range(3,int(i**0.5),2):
			if n % i == 0:
				return False
	else:
		return True



def GeneratePrime(n):
	n = int(input("Insert here: "))
	for i in range(n+1):
		if isPrime(i) == True:
			print(i)

