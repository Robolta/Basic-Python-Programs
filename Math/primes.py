from math import isqrt

def sieve_of_eratosthenes(upper_limit: int):
	if upper_limit < 2:
		return []
	
	is_prime = [False, False] + [True] * (upper_limit - 1)

	for candidate_value in range(2, isqrt(upper_limit + 1) + 1):
		if is_prime[candidate_value]:
			for composite_value in range(candidate_value * candidate_value, upper_limit + 1, candidate_value):
				is_prime[composite_value] = False
	
	return [i for i in range(upper_limit + 1) if is_prime[i]]

if __name__  == "__main__":
	print(sieve_of_eratosthenes(10))
	print(sieve_of_eratosthenes(100))