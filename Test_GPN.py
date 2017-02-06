import unittest
#import Math

class Test_IsPrime(unittest.TestCase):

    def test_for_zero(self):
	"""Test to check if 0 returns False"""
    	self.assertFalse(isPrime(0))

    def test_negative_numbers(self):
    	"""Test to check if a negative number is NOT determined prime"""
        self.assertFalse(isPrime(-1))

    def test_one_is_prime(self):
    	"""Test to confirm if 1 is treated an non prime"""
    	self.assertFalse(isPrime(1))


    def test_prime_number(self):
    	""""Test if 13 is correctly considered as a prime number """
    	self.assertTrue(isPrime(13))

    #def test_output_isprime_number(self):
    #	"""Test output correctness using Python inbuilt Prime method"""
    #	self.assertEqual()



class Test_GeneratePrime(unittest.TestCase):


	def test_string_type(self):
		"""Test to check if user input was not a string"""
		self.assertEqual(GeneratePrime('i'), 'Cannot input anything besides a whole number')

	def test_float_type(self):
		"""Test to check if user input was not a float"""
		self.assertEqual(GeneratePrime(2.58), 'Cannot input anything besides a whole number')

	def test_negative_input(self):
		"""Test to check if negative number was inputted"""
		self.assertEqual(GeneratePrime(-2), "Retry with a positive integer greater than 1")

	def test_zero_input(self):
		"""Test to check if zero was inputted"""
		self.assertEqual(GeneratePrime(0), "Retry with a positive integer greater than 1")

	def test_input_one(self):
		"""Test to check if int 1 was inputted"""
		self.assertEqual(GeneratePrime(1), "Retry with a positive integer greater than 1")


if __name__ == '__main__':
	unittest.main()
