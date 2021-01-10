from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Ocado(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'ocado'

	def get_content(self):
		return self.open_html_file('./sample_html/ocado.html')

	def find_slots(self):
		soup = self.get_content()

		slots_list = list()
		rawSlotsHtml: list = soup.select('table.inner-slot-booking-table a')

		for slotHtml in rawSlotsHtml:
			slotHtml = str(slotHtml)

			price: float = float(slotHtml[slotHtml.find('£')+len('£'):slotHtml.find('\">\n<span class="descr-')])
			string: str = slotHtml[slotHtml.find('aria-describedby=\"')+len('aria-describedby=\"'):slotHtml.find('\" aria-flow')]
			start_str: str = string[:string.find('_')]
			end_str: str = string[string.find('_')+1:string.find('m')+1]
			am_pm: str = end_str[-2:]

			start = str(datetime.strptime(start_str+am_pm,'%I%M%p').time())
			end = str(datetime.strptime(end_str,'%I%M%p').time())

			date: str = str(slotHtml[slotHtml.find('title=\"')+len('title=\"'):])
			date: str = date[:date.find('T')]
			date: str = str(datetime.strptime(date,'%Y-%m-%d').date())

			slot = Slot(self.supermarket_name, date, start, end, price)
			slots_list.append(slot.__dict__)

		return(slots_list)	
