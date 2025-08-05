class Square:
	def __init__(self, length):
		self.length = length
	
	def get_diagonal(self):
		return (2 ** 0.5) * self.length
	
	def get_perimeter(self):
		return 4 * self.length
	
	def get_area(self):
		return self.length * self.length