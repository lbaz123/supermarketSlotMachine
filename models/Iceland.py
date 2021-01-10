from abc import ABC, abstractmethod
from .SupermarketSlotFinder import SupermarketSlotFinder
from datetime import datetime
from .Slot import Slot

class Iceland(SupermarketSlotFinder):

	def __init__(self):
		self.supermarket_name = 'iceland'

	def get_content(self):
		return self.open_html_file('./sample_html/iceland.html')

	def find_slots(self):
		soup = self.get_content()
		price: float = 0.0
		slots_list = list()
		slotsByDay: list = soup.select('div.delivery-schedule-slots')
		for day in slotsByDay:
			day_string = str(day)
			date:str = day_string[day_string.find('data-slots-key=\"')+len('data-slots-key=\"'):day_string.find('\">')]
			date = str(datetime.strptime(date, '%Y%m%d').date())
			rawSlotsHtml = day.select('div.delivery-schedule-slot')
			for slot in rawSlotsHtml:
				slot = str(slot)
				if 'unavailable' not in slot:
					times = slot[slot.find(' - ')-5:slot.find('</div>\n<div class=\"delivery-slot-message\">')]
					times = times[:13]
					start = str(datetime.strptime(times[:5],'%H:%M').time())
					end = str(datetime.strptime(times[-5:],'%H:%M').time())
					slot = Slot(self.supermarket_name, date, start, end, price)
					slots_list.append(slot.__dict__)

		return(slots_list)	
