from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Asda(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'asda'

	def get_content(self):
		return self.open_html_file('./sample_html/asda.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list: list = list()

		rawSlotsHtml = soup.select('div.slot-button button')
		year = str(datetime.today().year)

		for slotHtml in rawSlotsHtml:
			slotHtml: str = str(slotHtml)

			if 'Slot full' not in slotHtml:
				string = slotHtml[slotHtml.find('from '):]
				start_str = string[string.find('from ')+len('from '):string.find(' to ')]
				start = str(datetime.strptime(start_str,'%I:%M%p').time())

				end_str = string[string.find(' to ')+len(' to '):string.find(' £')]
				end = str(datetime.strptime(end_str,'%I:%M%p').time())

				if 'hdExpressSlot' in slotHtml:
					date_str = slotHtml[slotHtml.find('basket. ')+len('basket. '):slotHtml.find(' from ')]
				else:	
					date_str = slotHtml[slotHtml.find('slot available ')+len('slot available '):slotHtml.find(' from ')]
				date = str(datetime.strptime(date_str+year, '%d %B%Y').date())
				price: float = float(string[string.find('£')+1:string.find('0"')])

				slot = Slot(self.supermarket_name, date, start, end, price)
				slots_list.append(slot.__dict__)

		return slots_list 	
