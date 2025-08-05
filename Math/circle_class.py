from math import PI

class Circle:
	def __init__(self, radius):
		self.radius = radius
	
	def get_radius(self):
		return self.radius
	
	def get_diameter(self):
		return 2 * self.radius
	
	def get_circumference(self):
		return 2 * PI * self.radius
	
	def get_area(self):
		return PI * self.radius * self.radius