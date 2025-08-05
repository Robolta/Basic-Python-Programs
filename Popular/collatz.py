def collatz(n):
	"""
	Yields values of the corresponding value's path following the steps of the Collatz Conjecture.
	If n is even, divide it by 2, otherwise, multiply it by 3 and add 1.
	The problem of the conjecture is whether or not all positive integers eventually reach 1.

	Yields:
		int: The value after following the prior steps
	"""
	yield n

	while n != 1:

		if n % 2 == 1:
			n = n * 3 + 1
			yield n

		while n % 2 == 0:
			n //= 2
			yield n