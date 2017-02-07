def isPrime(n):
	if n <= 1:
		return False
	if n==2 or n==3 :
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
	if n <= 1:
		return "Retry with a positive integer greater than 1"
	elif n ==2:
		return n
		
	try:
		primeList = []
		for i in range(n+1):
			if isPrime(i) == True:
				primeList.append(i)
		return primeList
	except TypeError:
		Print ('Cannot input anything besides a whole number')

