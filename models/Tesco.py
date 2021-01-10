from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Tesco(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'tesco'

	def get_content(self):
		return self.open_html_file('./sample_html/tesco.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list: list = list()

		date = str(soup.select("li.day-selector__list-item.day-selector__list-item--selected")[0])
		date = date[date.find('data-date=\"')+len('data-date=\"'):date.find('\" role="pres')]
		rawSlotsHtml = soup.select("div.slot-list ul li")

		for slotHtml in rawSlotsHtml:
			slotHtml: str = str(slotHtml)
			if 'unavailable' not in slotHtml:
				start_str = slotHtml[slotHtml.find('times\">')+len('times\">'):slotHtml.find(' - ')]
				start = str(datetime.strptime(start_str,'%H:%M').time())

				end_str = slotHtml[slotHtml.find(' - ')+len(' - '):slotHtml.find('</span>')]
				end = str(datetime.strptime(end_str,'%H:%M').time())

				price: str = slotHtml[slotHtml.find('data-auto=\"price-value\">')+len('data-auto=\"price-value\">'):]
				price: float = float(price[:price.find('</span>')])

				slot = Slot(self.supermarket_name, date, start, end, price)
				slots_list.append(slot.__dict__)


		return slots_list 	
