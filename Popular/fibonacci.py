def classic_fibonacci():
	"""
	Returns each number of the Fibonacci sequence in order indefinitely.

	Yields:
		int: The next Fibonacci number, starting with (0, 1, 1, 2...)
	"""
	a, b = 0, 1
	while True:
		yield a
		a += b # fib(n) = fib(n-2) + fib(n-1) where fib(n-1) is simply the previous value of a
		b = a - b # fib(n-1) = fib(n) - fib(n-2)



def nth_fibonacci(n):
	"""
	Computes each Fibonacci value in order to find the nth number in the sequence (where 0 and 1 are the results for n = 0 and 1 respectively).

	Args:
		n (int): The position of the Fibonacci number.
	
	Returns:
		int: The nth Fibonacci number.
	"""
	for i, fib in zip(range(n + 1), classic_fibonacci()):
		pass
	return fib



def nth_recursive(n):
	"""
	Uses recursion to find the nth number in the Fibonacci sequence (where 0 and 1 are the results for n = 0 and 1 respectively).
	Recursion is when a function calls itself, typically changing the parameters each time.

	Args:
		n (int): The position of the Fibonacci number.
	
	Returns:
		int: The nth Fibonacci number.
	"""
	if n == 0:return 0
	if n == 1:return 1
	return nth_recursive(n - 1) + nth_recursive(n - 2)



cache = {0:0, 1:1}
def nth_memoization(n):
	"""
	Uses memoization and recursion to find the nth number in the Fibonacci sequence (where 0 and 1 are the results for n = 0 and 1 respectively).
	Memoization is storing the results of expensive function calls in memory, rather than having to call them again in the future.

	Args:
		n (int): The position of the Fibonacci number.
	
	Returns:
		int: The nth Fibonacci number.
	"""
	if n in cache:return cache[n]
	result = nth_memoization(n - 1) + nth_memoization(n - 2)
	cache[n] = result
	return result



def nth_math(n):
	"""
	Uses Binet's Formula to find the nth number in the Fibonacci sequence (where 0 and 1 are the results for n = 0 and 1 respectively).
	The formula provides an exact closed form for the nth Fibonacci number, but in practice won't get very far due to precision errors in floating point numbers.
	The formula is: F(n) = (1 / √5) * (φ^n - ψ^n)

	Args:
		n (int): The position of the Fibonacci number.
	
	Returns:
		int: The nth Fibonacci number.
	"""
	PHI = (1 + 5 ** 0.5) / 2 # The golden ratio
	PSI = (1 - 5 ** 0.5) / 2 # The negative reciprocal of the golden ratio

	return round((1 / 5 ** 0.5) * (PHI ** n - PSI ** n))



if __name__ == "__main__":
	print(nth_fibonacci(5))
	print(nth_recursive(5))
	print(nth_memoization(5))
	print(nth_math(5))