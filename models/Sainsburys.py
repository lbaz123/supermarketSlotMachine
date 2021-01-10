from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Sainsburys(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'sainsburys'

	def get_content(self):
		return self.open_html_file('./sample_html/sainsburys.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list: list = list()

		rawSlotsHtml = soup.select('table.deliverySlots a')

		for slotHtml in rawSlotsHtml:
			slotHtml: str = str(slotHtml)

			start_str = slotHtml[slotHtml.find('between ')+len('between '):slotHtml.find(' - ')]
			start = str(datetime.strptime(start_str,'%I:%M%p').time())

			end_str = slotHtml[slotHtml.find(' - ')+len(' - '):slotHtml.find(', av')]
			end = str(datetime.strptime(end_str,'%I:%M%p').time())

			date_str = slotHtml[slotHtml.find('day ')+len('day '):slotHtml.find(', between ')]
			date = str(datetime.strptime(date_str, '%d %B %Y').date())

			link = slotHtml[slotHtml.find('href=\"')+len('href=\"'):slotHtml.find('\">')]

			price: float = float(slotHtml[slotHtml.find('£')+1:slotHtml.find('</a>')])

			slot = Slot(self.supermarket_name, date, start, end, price, link)
			slots_list.append(slot.__dict__)


		return slots_list 	
