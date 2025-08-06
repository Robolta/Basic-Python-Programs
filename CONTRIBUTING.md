# Contributing Guidelines

The repository's guidelines on making pull requests.  Note that these guidelines are subject to change and are more than likely to change in the future.  Any recommendations are more than welcome in the form of issues, pull requests, or direct messages (if you know how to contact me already).

## Writing Code

The code here is intended to be a resource for beginners to learn about the various algorithms or even just use the code directly.

With that in mind, our aim is to keep things **readable, organized, and consistent**.

### Code Readability (Style Guide)

**Variable Names** - Variables should have clear and descriptive names.  Do NOT prioritize short variables.

**Comments** - Comments are allowed, but by and large the code should be clear enough on its own.

**Type Hints** - Make use of type hints where possible.  Conveying the intended type of different variables helps clarify further what the aim is.

**Docstrings** - Use docstrings with a description of the function or class, arguments, and return or yield value(s).

**Spacing** - Space things out.  These are fairly small programs so giving the lines more room to breathe with newlines is encouraged.

**Intending** - After around 4 indents, it's recommended that some parts be placed in a separate function.  This keeps the job of different pieces of code more clear.

**Libraries** - While libraries are important to learn and use, in this repository, we are showcasing various algorithms, not just creating functional code.  Try to avoid using libraries when they'd be handling a bulk of the algorithm itself.

**One Class > Many Functions** - If you have a lot of related functions, consider whether or not it'd make sense for them to be methods of a single class.  A good example of this is the various shape classes.  Each has different methods for area, perimeter, etc, which wouldn't be much as individual functions.

### This code would not be accepted.

```py
def collatz(n):
	while n != 1:
		if n % 2 == 1:n = n * 3 + 1
		while n % 2 == 0:n //= 2
	return True
```

Main Issues:

- Very Dense
- No Type Hinting
- Non-descriptive Names

### This code would be accepted.

```py
def does_follow_collatz(value: int) -> bool:
	"""
	Returns True if the provided value eventually reaches 1, following the steps outlined for the Collatz Conjecture.

	Args:
		value (int): Starting value being tested.
	
	Return:
		bool: Returns True if it reaches 1.  Doesn't check for anything else.
	"""
	while value != 1:

		if value % 2 == 1:
			value = 3 * value + 1
		
		while value % 2 == 0:
			value //= 2
	
	return True
```

In practice, the difference between `n` and `value` is probably not enough to accept/deny a pull request.

**Examples** - Additionally, at the bottom of your file should be a call of any functions, classes, and methods included.  This can be done with the `if __name__ == "__main__"` code block. For the example above, this could be written as follows:

```py
if __name__ == "__main__":
	print(does_reach_one_collatz(3))
```

### Code File Organization

Generally, we try to keep the repository organized into categories based on the code we're currently including or planning to include.

If a category for a program you want doesn't yet exist, rather than creating that category in your pull request, we encourage first creating an issue requesting the category.

The idea here is that some categories may not be approved, meaning it'd be best not to create a full pull request just to find that out.

### Consistency

Generally, consistency simply comes from following the guidelines on writing code and being sure your pull request does what you intended (i.e. putting the files in the right place).

## Making a Pull Request

- Fork the repository (this creates your own copy which you can freely modify)
- Make the relevant changes
- Submit a pull request explaining what was changed
- Respond to any feedback

That's the overview.  A detailed explanation of these steps might be added in the future.

We also encourage making comments on other people's issues and pull requests if you have any feedback to provide.