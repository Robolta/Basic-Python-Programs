class Square:
	def __init__(self, length: int | float):
		self.length = length
	
	def get_diagonal(self) -> float:
		return (2 ** 0.5) * self.length
	
	def get_perimeter(self) -> int | float:
		return 4 * self.length
	
	def get_area(self) -> int | float:
		return self.length * self.length
	


if __name__ == "__main__":
	square = Square(5.5)
	print(square.get_diagonal())
	print(square.get_perimeter())
	print(square.get_area())