class Slot:
	def __init__(self, supermarket, date, start_time, end_time, price = None, link = None):
		self.supermarket = supermarket
		self.date = date
		self.start_time = start_time
		self.end_time = end_time
		self.price = price
		self.link = link