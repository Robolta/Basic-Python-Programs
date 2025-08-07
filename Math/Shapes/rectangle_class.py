class Rectangle:
	def __init__(self, length: int | float, width: int | float):
		self.length = length
		self.width = width
	
	def get_diagonal(self) -> float:
		return (self.length * self.length + self.width * self.width) ** 0.5
	
	def get_perimeter(self) -> int | float:
		return 2 * (self.length + self.width)

	def get_area(self) -> int | float:
		return self.length * self.width



if __name__ == "__main__":
	rectangle = Rectangle(5, 7.5)
	print(rectangle.get_diagonal())
	print(rectangle.get_perimeter())
	print(rectangle.get_area())