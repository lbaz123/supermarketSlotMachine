from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Morrisons(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'morrisons'

	def get_content(self):
		return self.open_html_file('./sample_html/morrisons.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list: list = list()

		rawSlotsHtml = soup.select('table tbody tr td')

		for slotHtml in rawSlotsHtml:

			slotHtml=str(slotHtml)

			if '£' in slotHtml:

				start_str = slotHtml[slotHtml.find('Time, ')+len('Time, '):slotHtml.find(' - ')]
				start = str(datetime.strptime(start_str,'%H:%M').time())

				end_str = slotHtml[slotHtml.find(' - ')+len(' - '):slotHtml.find(', Price')]
				end = str(datetime.strptime(end_str,'%H:%M').time())
				
				year = slotHtml[slotHtml.find('datetime=\"')+len('datetime=\"'):slotHtml.find('datetime=\"')+len('datetime=\"')+4]

				date_str = slotHtml[slotHtml.find('Date, ')+len('Date, ')+4:slotHtml.find(', Time, ')]
				date = str(datetime.strptime(date_str+year, '%d %b%Y').date())

				price: float = float(slotHtml[slotHtml.find('Price, £')+len('Price, £'):slotHtml.find('\" data-test=\"')])
				slot = Slot(self.supermarket_name, date, start, end, price)
				slots_list.append(slot.__dict__)

		return slots_list 	
