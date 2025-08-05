class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width
	
	def get_diagonal(self):
		return (self.length * self.length + self.width * self.width) ** 0.5
	
	def get_perimeter(self):
		return 2 * (self.length + self.width)

	def get_area(self):
		return self.length * self.width