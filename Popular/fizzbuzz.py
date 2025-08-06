def fizzbuzz(upper_limit):
	"""
	Yields strings based on the rules of "Fizzbuzz".
	Iterates starting at 1 up to the upper_limit.
	If a number is divisible by 3, yield "Fizz".
	If a number is divisible by 5, yield "Buzz".
	Otherwise, simply yield the number.

	Args:
		upper_limit (int): The highest number used when iterating.

	Yields:
		str: The string for the current number.
	"""
	for value in range(1, upper_limit + 1):

		output = ""
		
		if value % 3 == 0:
			output += "Fizz"

		if value % 5 == 0:
			output += "Buzz"

		if output == "":
			output = str(value)

		yield output



if __name__ == "__main__":
	for value in fizzbuzz(100):
		print(value)