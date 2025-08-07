from math import PI

class Circle:
	def __init__(self, radius: int | float):
		self.radius = radius
	
	def get_diameter(self) -> int | float:
		return 2 * self.radius
	
	def get_circumference(self) -> float:
		return 2 * PI * self.radius
	
	def get_area(self) -> float:
		return PI * self.radius * self.radius