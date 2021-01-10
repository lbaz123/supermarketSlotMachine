from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Waitrose(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'waitrose'

	def get_content(self):
		return self.open_html_file('./sample_html/waitrose.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list: list = list()

		rawSlotsHtml = soup.select('table.slotTable___b_B2N tbody tr td')
		price = 0
		
		for slotHtml in rawSlotsHtml:
			slotHtml: str = str(slotHtml)
			if 'Unavailable' not in slotHtml and 'Fully booked' not in slotHtml:
				time_str = slotHtml[slotHtml.find('data-time=\"')+len('data-time=\"'):slotHtml.find('\">')]

				start_str = slotHtml[slotHtml.find('data-time=\"')+len('data-time=\"'):slotHtml.find(' - ')]
				start_str += time_str[-2:]
				start = str(datetime.strptime(start_str,'%I%p').time())

				end_str = slotHtml[slotHtml.find(' - ')+len(' - '):slotHtml.find('\">')]
				end = str(datetime.strptime(end_str,'%I%p').time())
				
				date_str = slotHtml[slotHtml.find('data-id=\"')+len('data-id=\"'):slotHtml.find('_')]
				date = str(datetime.strptime(date_str, '%Y-%m-%d').date())

				slot = Slot(self.supermarket_name, date, start, end, price)
				slots_list.append(slot.__dict__)

		return slots_list 		
