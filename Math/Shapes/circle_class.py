from math import pi

class Circle:
	def __init__(self, radius: int | float):
		self.radius = radius
	
	def get_diameter(self) -> int | float:
		return 2 * self.radius
	
	def get_circumference(self) -> float:
		return 2 * pi * self.radius
	
	def get_area(self) -> float:
		return pi * self.radius * self.radius



if __name__ == "__main__":
	circle = Circle(5.5)
	print(circle.get_diameter())
	print(circle.get_circumference())
	print(circle.get_area())