# Style Guide

Various conventions which range from strongly encouraged to required.

## Naming Conventions

Naming conventions relate to how we name various aspects of our programs.

Different naming conventions are used for different program parts:

|Structure|Naming Convention|Examples|
|---|---|---|
|Constants|Uppercase, underscores for spaces|`SQUARE_NUMBERS`|
|Non-Constant Variables or Functions|Lowercase, underscores for spaces|`waiting_list` or `generate_primes()`|
|Classes|Capitalized words, no spaces|`PickupTruck`|

## Variables

As a convention, a single numeric argument to a function should be written as `value` rather than a single variable such as `i` or `n` or `x`.

### Type Hints

Variables should always make use of type hints.  In some cases, the `typing` library should be used.

```py
from typing import List

pi_approximation: float = 22 / 7
is_seven_prime: bool = not (7 % 2 == 0 or 7 % 3 == 0)
square_numbers: List[int] = [i * i for i in range(1, 101)]
```

In reality these should probably all be written as constants (meaning they'd be uppercase) and `is_seven_prime` could be written with a simple `True`.

## Functions

### Function Prefixes

It is encouraged to prefix functions based on what their purpose is, as shown below:

|Function Category|Name Prefix|Example|
|---|---|---|
|Returns Boolean|`is_` or `does_`|`is_prime` or `does_repeat`|
|Returns Stored Value (or small calculation)|`get_`|`get_length` or `get_area`|
|Calculation|`compute_`|`compute_factorial`|
|Search|`find_`|`find_median`|
|Yields Any or Returns List|`generate_`|`generate_fibonacci_numbers`|

The general idea is that each function is named as an action (or a question in the case of returning booleans) which describes what it does.  A function `find_optimal_path` can be assumed to be a search algorithm, looking for an optimal path while `get_volume` is likely a simple volume calculation.

It doesn't cover every possible case, so use your best judgement where relevant.

### Type Hints

Type hints should be used for all variables, but also the parameters and return type.

```py
def is_prime(n: int) -> bool:

	upper_bound: int = round(n ** 0.5) + 1
	for i in range(2, upper_bound):
		if n % i == 0:return False

	return True
```

For some cases, such as lists and generators, the `typing` library is used.  This gives access to `List`, `Any`, `Iterator`, `Generator`, and others.

```py
from typing import Iterator

def generate_fibonacci_numbers() -> Iterator[int]:

	previous_number: int = 1
	current_number: int = 0

	while True:
		yield current_number
		current_number += previous_number
		previous_number = current_number - previous_number
```

### Spacing Arguments

When a function name is longer or has many arguments, it is recommended to break the arguments up into separate lines like the example below:

```py
def compute_sum_of_5_numbers(
	number1: int,
	number2: int,
	number3: int,
	number4: int,
	number5: int
) -> int:
	return number1 + number2 + number3 + number4 + number5
```

### Docstrings

Docstrings should be used on every function.  It should include an explanation of the function, a list of arguments, and a list of what is returned/yielded.

```py
def get_step_count(value: int) -> int:
	"""
	Returns the number of steps taken on the corresponding value's path following the steps of the Collatz Conjecture to reach 1.
	If n is even, divide it by 2, otherwise, multiply it by 3 and add 1.
	The problem of the conjecture is whether or not all positive integers eventually reach 1.

	Args:
		value (int): The starting value

	Returns:
		int: The value after following the prior steps
	"""
	steps = 0
	while value != 1:

		if value % 2 == 1:
			value = 3 * value + 1
			steps += 1
		
		while value % 2 == 0:
			value //= 2
			steps += 1

	return steps
```

## Classes